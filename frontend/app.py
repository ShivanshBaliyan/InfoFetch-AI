import api
print(api.__file__)

import asyncio
import streamlit as st

from api import send_message

st.set_page_config(
    page_title="Website Data Chatbot",
    page_icon="💬",
)

st.title("💬 Website Data Chatbot")

message = st.text_input("Enter your message")

if st.button("Send"):
    response = asyncio.run(send_message(message))

    st.success(response["message"])
    st.write(response["data"]["reply"])