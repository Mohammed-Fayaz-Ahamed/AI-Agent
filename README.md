#  AI Research Assistant – Multi-Agent LLM App

This is a Streamlit-based AI assistant powered by open-source LLMs for industry analysis, use case generation, and resource discovery. It uses LangChain and Hugging Face models to simulate expert agents for deep market research.

##  Features

-  **Industry Research Agent** – Analyzes a given company's industry, trends, and challenges.
-  **AI Use Case Strategist** – Suggests domain-relevant AI/GenAI use cases.
-  **Resource Collector** – Finds useful APIs, datasets, and ML libraries for implementation.
-  **Downloadable Reports** – Users can download the analysis as a formatted text report.
-  **Deployed via Streamlit Cloud** (or run locally)

---

##  Architecture

- **Frontend**:
  - Streamlit UI for input, display, and download
- **Backend**:
  - LangChain LLMChains for prompt management
  - Hugging Face models (e.g., `google/flan-t5-large`, `tiiuae/falcon-7b-instruct`)
  - Modular agent functions


