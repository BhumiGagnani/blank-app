import streamlit as st
from pathlib import Path
from itertools import chain

# Load slides and comments
slides_folder = Path("Slides")  # Replace with your folder path
comments_file = Path("comments.md")  # Replace with your markdown file path

# Support slide images and comments
slides = sorted(chain(
    slides_folder.glob("*.jpg"),
    slides_folder.glob("*.JPG"),
    slides_folder.glob("*.png"),
    slides_folder.glob("*.PNG")
))

# Read comments
with comments_file.open("r") as f:
    comments = f.read().split("\n---\n")
    
# Debugging: Check if any slides were found
if not slides:
    st.error("No slides found in the slides folder!")
    st.stop()
    print(f"Slides detected: {len(slides)} -> {[str(slide) for slide in slides]}")

# Debugging: Check comments
if not comments:
    st.error("No comments found in the comments file!")
    st.stop()
print(f"Comments detected: {len(comments)}")

# Check for matching counts
if len(slides) != len(comments):
    st.error(f"Number of slides ({len(slides)}) and comments ({len(comments)}) do not match!")
    st.stop()

# Check if slides and comments align
if len(slides) != len(comments):
    st.error("Number of slides and comments do not match!")
    st.stop()

# Session state to track current slide
if "current_slide" not in st.session_state:
    st.session_state.current_slide = 0

# Display current slide and comment
slide_idx = st.session_state.current_slide
st.image(str(slides[slide_idx]), caption=f"Slide {slide_idx + 1}")
st.markdown(comments[slide_idx])

# Navigation buttons
col1, col2 = st.columns(2)
with col1:
    if st.button("Previous") and slide_idx > 0:
        st.session_state.current_slide -= 1
with col2:
    if st.button("Next") and slide_idx < len(slides) - 1:
        st.session_state.current_slide += 1
