# Imports
from pieces_copilot_sdk import PiecesClient
import platform
import streamlit as st

# Set port based on platform information
platform_info = platform.platform()
if 'Linux' in platform_info:
    port = 5323
else:
    port = 1000

# Initialize Pieces Copilot Client
pieces_client = PiecesClient(
    config={
        "baseUrl": f"http://localhost:{port}"
    }
)

# Setup UI for Streamlit
st.title("Pieces Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Ask me a question?"):

    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = pieces_client.ask_question(prompt)

    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})
