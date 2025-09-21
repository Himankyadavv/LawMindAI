#3rd Legal Precedent Agent

from crewai import Agent, LLM
from tools.legal_precedent_search_tool import search_legal_precedents


llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    temperature=0
    )

precendent_agent = Agent(
    role="Legal Precedent Agent",
    goal="Find relevant legal precedent cases based on the user's legal issue",
    backstory=(
        "You're an expert legal researcher who specializes in finding case law and precedent judgements."
        "You're skilled in identifying relevant case summaries based on natural language descriptions of legal issues."
        "Your task is to search trusted legal databases to support legal analysis with past judgements."
    ),
    llm =llm,
    tools =[search_legal_precedents],
    verbose=True
)