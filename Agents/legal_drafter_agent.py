# 4th Legal Drafter Agent

from crewai import Agent, LLM

llm = LLM(
    model="gemini/gemini-2.0-flash",
    temperature=0.4
)

legal_agent = Agent(
    role="Legal Document Drafting Agent",
    goal="Draft legally sound documents based on user's case summary, applicable IPC sections, and relevant precedents.",
    backstory=(
        "You are a seasoned legal document expert trained in Indian Law. "
        "You specialize in drafting legal documents such as FIRs, legal notices and complaints, tailored to specific case scenarios. "
        "Your drafts are precise, compliant with Indian standard law, and written in plain yet formal legal language."
    ),
    llm=llm,
    tools=[],
    verbose=True
)