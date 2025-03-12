# Essential Libraries
import streamlit as st
from agents import *
import time

# Initialize Streamlit App
st.set_page_config(page_title="Medical AI Assistant", layout="wide")
st.title("Multi Agent Medical AI Assistant 🩺")
st.write("Note: Ask medical questions and get AI-powered responses, but please consult a medical professional for advice. Do not fully rely on AI assistants for medical assistance.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)

    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Create a placeholder for the assistant's response
    response_placeholder = st.chat_message("assistant").empty()

    # Show a spinner while waiting for the response
    with st.spinner("Thinking..."):
        # Get the response from the agent
        response = run_agent(prompt)

        # Simulate streaming by breaking the response into chunks
        chunks = response.split()
        streaming_response = ""

        # Display the response in chunks with a delay
        for chunk in chunks:
            streaming_response += chunk + " "
            response_placeholder.markdown(streaming_response)
            time.sleep(0.1)  # Adjust the delay as needed

    # Add the final response to the chat history
    st.session_state.messages.append({"role": "assistant", "content": streaming_response})