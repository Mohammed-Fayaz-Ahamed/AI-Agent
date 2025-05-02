# agents.py

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from model_loader import load_llm

llm = load_llm()

def get_agent(prompt_template: str):
    prompt = PromptTemplate(template=prompt_template, input_variables=["company"])
    return LLMChain(llm=llm, prompt=prompt)

industry_researcher = get_agent(
    "You are an industry analyst. Provide a detailed overview of the industry, market trends, and challenges faced by {company}."
)

ai_usecase_strategist = get_agent(
    "You are an AI strategist. List 5-7 impactful AI/GenAI use cases for {company}. Explain each in 1-2 lines."
)

resource_collector = get_agent(
    "You are a tech scout. Suggest useful APIs, datasets, and ML libraries for developing AI use cases for {company}. Categorize your suggestions."
)

def run_all_agents(company: str) -> dict:
    return {
        "Industry Research": industry_researcher.run(company=company),
        "AI Use Cases": ai_usecase_strategist.run(company=company),
        "Resources": resource_collector.run(company=company),
    }
