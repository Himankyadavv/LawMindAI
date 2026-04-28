# 1st agent case_intake_agent

from crewai import Agent, LLM

llm = LLM(
    model="gemini/gemini-2.0-flash",
    temperature=0
)

# making agent
intake_agent = Agent(
    role="Case Intake Agent",
    goal=(
        "Understand the user's legal issue and classify it into structured format "
        "for further legal processing. "
    ),
    backstory=(
        "You are a highly skilled legal intake assistant trained to analyze plain english legal concerns. "
        "You identify the type of legal issue, categorize it into domain of law and extract relevant content"
        " to pass along to legal researchers, drafters or compliance teams."
    ),
    llm=llm,
    tools=[],
    verbose=True
)
