import asyncio

import streamlit as st

from api import get_health

st.set_page_config(
    page_title="Website Data Chatbot",
    page_icon="💬",
)

st.title("💬 Website Data Chatbot")

if st.button("Check Backend Status"):

    health = asyncio.run(get_health())

    st.success(health["message"])

    st.json(health["data"])