import streamlit as st

st.set_page_config(page_title="Elevate Labs AI/ML Project", layout="centered")

st.title("News Article Classification – Demo")
st.write("Deployment check ✅. Replace this text with your real app logic.")

txt = st.text_area("Try typing something:")
if st.button("Submit"):
    st.success(f"You typed: {txt}")
  
