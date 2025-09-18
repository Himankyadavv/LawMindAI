# 2nd IPC Section Agent

#import libraries 
from crewai import Agent, LLM
from tools.ipc_sections_search_tool import search_ipc_sections


llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    temperature=0.3,
)

ipc_section_agent = Agent(
    role="IC Section Agent",
    goal="Identify the most relevant Indian Penal Code(IPC) section based on legal issue provided",
    backstory=(
        "You are seasoned legal researcher with deep knowledge of Indian penal laws."
        "You specialize in mapping legal issue to applicable IPC sections with precision and clarity."
        "Your insight helps lawyer and assistant quickly understand the statutory basis of a case."),
    llm=llm,
    tools=[search_ipc_sections],
    verbose=True
)


