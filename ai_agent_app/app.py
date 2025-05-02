import streamlit as st
from transformers import pipeline
from langchain.llms import HuggingFacePipeline
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Set page config
st.set_page_config(page_title="AI Research Framework", layout="centered")

@st.cache_resource
def load_llm():
    generator = pipeline("text2text-generation", model="google/flan-t5-base", max_new_tokens=300)
    return HuggingFacePipeline(pipeline=generator)

llm = load_llm()

def get_agent(prompt_template: str):
    prompt = PromptTemplate(template=prompt_template, input_variables=["company"])
    return LLMChain(llm=llm, prompt=prompt)

# Define agents
industry_researcher = get_agent(
    "You are an industry analyst. Given a company named {company}, give an overview of its industry, market trends, and key challenges."
)

ai_usecase_strategist = get_agent(
    "You are an AI strategist. List top AI/GenAI use cases relevant for {company} in their domain."
)

resource_collector = get_agent(
    "You are a tech scout. Suggest useful datasets, APIs, or ML libraries for building the use cases for {company}."
)

def run_all_agents(company_name: str) -> dict:
    return {
        "Industry Research": industry_researcher.run(company=company_name),
        "AI Use Cases": ai_usecase_strategist.run(company=company_name),
        "Resources": resource_collector.run(company=company_name)
    }

# --- Streamlit UI ---
st.title("🔍 AI Research Framework")

company_name = st.text_input("Enter Company Name", placeholder="e.g. Tesla")

if st.button("Generate Report") and company_name:
    with st.spinner("Running AI agents..."):
        output = run_all_agents(company_name)
    
    st.success("Report generated!")

    # Display sections
    for section, content in output.items():
        st.subheader(section)
        st.write(content)

    # Prepare download content
    full_report = "\n\n".join([f"### {k}\n{v}" for k, v in output.items()])

    st.download_button(
        label="📄 Download Report",
        data=full_report,
        file_name=f"{company_name}_ai_research.txt",
        mime="text/plain"
    )
