import streamlit as st
import os
from dotenv import load_dotenv
from groq import Groq
from chargers_bot import ChargersBot


#SETUP BOT

# Load the .env file
load_dotenv()

# Access the API key
apiKey = os.getenv('GROQ_API_KEY')
client = Groq(api_key = apiKey)

# initial chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

bot = ChargersBot(llm = client)


# STREAMLIT UI BEGIN FROM HERE

# Initial message (at top of screen)
with st.chat_message("assistant"):
    st.write("Halo saya Wafa :hand:")


# Display chat messages from history on app rerun
for messages in st.session_state.messages:
    with st.chat_message(messages["role"]):
        st.markdown(messages["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        result = bot.chat(prompt)
        st.write(result)
            
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": result})