import streamlit as st
from utils import query_ibm_granite
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Smart City Assistant", layout="centered")
st.title("🏙️ Sustainable Smart City Assistant")
st.markdown("Ask anything about sustainability, smart infrastructure, or eco-friendly living in cities.")

user_input = st.text_input("Ask your question here:")

if st.button("Get Answer") and user_input:
    with st.spinner("Thinking..."):
        response = query_ibm_granite(user_input)
        st.success("Here's what I found:")
        st.write(response)
