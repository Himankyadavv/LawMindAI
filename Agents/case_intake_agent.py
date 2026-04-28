# 1st agent case_intake_agent

# import libraries 
from dotenv import load_dotenv
load_dotenv()

from crewai import Agent, LLM

llm = LLM(
    model="gemini/gemini-2.0-flash",
    temperature=0
)

# making agent
intake_agent = Agent(
    role="Case Intake Agent",
    goal=(
        "Understand the user's legal issue and classify it into structured format"
        "for further legal processing. "
    ),
    backstory=(
        "You are a highly skilled legal intake assistant trained to analyze plain english legal concerns. "
        "You identify the type of legal issue, categorize it into domain of law and extract relevant content"
        " to pass along to legal researchers, drafters or complaince teams."
    ),
    llm=llm , # You can define this in env also if you are using one llm for all agents 
    tools=[],
    verbose=True # Sets verbose as True when you want full explanation 
) 


