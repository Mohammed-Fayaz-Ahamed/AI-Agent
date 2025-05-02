# model_loader.py

from langchain.llms import HuggingFaceEndpoint
import streamlit as st

def load_llm():
    repo_id = "HuggingFaceH4/zephyr-7b-beta"
    return HuggingFaceEndpoint(
        repo_id=repo_id,
        huggingfacehub_api_token=st.secrets["HUGGINGFACE_API_KEY"],
        task="text-generation",
        temperature=0.7,
        max_new_tokens=2000
    )
