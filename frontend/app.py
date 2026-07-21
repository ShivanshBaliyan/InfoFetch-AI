import streamlit as st
from api import send_message

st.set_page_config(
    page_title="Website Data Chatbot",
    page_icon="💬",
)

st.title("💬 Website Data Chatbot")

# Initialize conversation
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous conversation
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
prompt = st.chat_input("Ask me anything...")

if prompt:
    # Save and display user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Get assistant response
    response = send_message(prompt)
    reply = response["data"]["reply"]

    # Save assistant message
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": reply,
        }
    )

    # Display assistant message
    with st.chat_message("assistant"):
        st.markdown(reply)