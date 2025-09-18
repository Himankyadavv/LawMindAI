#3rd Legal Precedent Agent

from crewai import Agent, LLM

llm = LLM(
    model="",
    temperature=
    )

precendent_agent = Agent(
    role="",
    goal="",
    backstory="",
    llm =llm,
    tools ="",
    verbose=True
)