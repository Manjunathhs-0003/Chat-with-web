import streamlit as st

st.set_page_config(page_title="Chat With Websites", page_icon="🤖")

st.title("Chat With Websites")

with st.sidebar:
    st.header("Settings")
    website_url = st.text_input("Website URL")
    
st.chat_input("Type Your message here.....")

with st.chat_message("AI"):
    st.write("Hello, How can i help you")

with st.chat_message("Human"):
    st.write("I want to know about Langchain")


