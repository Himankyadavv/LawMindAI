# 2nd IPC Section Agent

#import libraries 
from dotenv import load_dotenv
load_dotenv()

from crewai import Agent, LLM
from tools.ipc_sections_search_tool import search_ipc_sections

llm = LLM(
    model="gemini/gemini-2.0-flash",
    temperature=0.3,
)

ipc_section_agent = Agent(
    role="IPC Section Agent",
    goal="Identify the most relevant Indian Penal Code(IPC) section based on legal issue provided",
    backstory=(
        "You are seasoned legal researcher with deep knowledge of Indian penal laws."
        "You specialize in mapping legal issue to applicable IPC sections with precision and clarity."
        "Your insight helps lawyer and assistant quickly understand the statutory basis of a case."),
    tools=[search_ipc_sections],
    llm=llm,
    
    verbose=True
)


