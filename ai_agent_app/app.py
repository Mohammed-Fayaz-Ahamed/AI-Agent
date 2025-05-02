import streamlit as st
from agents import run_all_agents

st.set_page_config(page_title="Mistral LLM Report Generator", layout="centered")
st.title("📊 AI Research Generator using Mistral")

company = st.text_input("Enter Company Name", placeholder="e.g. Samsung")

if st.button("Generate Report") and company:
    with st.spinner("Running LangChain agents using Mistral..."):
        output = run_all_agents(company)

    st.success("Report Ready!")

    for section, content in output.items():
        st.subheader(section)
        st.write(content)

    full_report = "\n\n".join([f"{section}\n{'-'*30}\n{content}" for section, content in output.items()])
    st.download_button("📥 Download Report", full_report, file_name=f"{company}_ai_research.txt")
