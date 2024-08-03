import streamlit as st

st.set_page_config(page_title="Chat With Websites", page_icon="🤖")

st.title("Chat With Websites")

with st.sidebar:
    st.header("Settings")
    website_url = st.text_input("Website URL")