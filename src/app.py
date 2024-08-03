import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def get_response(user_input):
   return "IDK"

def get_vectorstore_url(url):
    #get the text in document form
    loader = WebBaseLoader(url)
    document = loader.load()

    #split document into chunk
    text_splitter = RecursiveCharacterTextSplitter()
    document_chunk = text_splitter.split_documents(document)

    return document_chunk

#app config
st.set_page_config(page_title="Chat With Websites", page_icon="🤖")
st.title("Chat With Websites")

#evrytime we enter a input, everything will be considered as a new cycle,
#in order to maintain a chat history, make it persistent

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
   AIMessage(content="Hello, I am a bot. How can i help you?"),
]

#sidebar
with st.sidebar:
    st.header("Settings")
    website_url = st.text_input("Website URL")

if website_url is None or website_url == "":
    st.info("Please enter a website URL")
else:
    documents_chunks = get_vectorstore_url(website_url)
    st.write(documents_chunks)
    #user input
    user_query = st.chat_input("Type Your message here.....")
    if user_query is not None and user_query != "":
        response = get_response(user_query)
        st.session_state.chat_history.append(HumanMessage(content=user_query))
        st.session_state.chat_history.append(AIMessage(content=response))

    #Conversation
    for message in st.session_state.chat_history:
        if isinstance(message, AIMessage):
            with st.chat_message("AI"):
                st.write(message.content)
        elif isinstance(message, HumanMessage):
            with st.chat_message("Human"):
                st.write(message.content)

    



#HTML documents -> use langchain to extract the texts -> convert text into chunks -> 
# chunks are passed through the embeddings model -> Embeddings convert these cunks into numerical representations (0's and 1's) -> 
# store it in vector -> convert user's query to do the same thing -> 
# then perform the semantic search using vector data to find the data similar to the query -> 
# send the returned chunk into llm -> find the one that matched the chunk





