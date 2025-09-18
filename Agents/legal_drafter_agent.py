# 3rd Legal Drafter Agent 

from crewai import Agent, LLM

llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    temperature=0.4
)

legal_agent = Agent(
    role="Legal Document Drafting Agent ",
    goal="Draft legally sound documents based on user's case summary, applicable IPC section, and relevant precedent.",
    backstory=(
        "You are a seasoned legal document expert trained in Indian Law"
        "You are specialize in drafting legal documents such as FIRs, legal notice and complaints, tailored to specific case sceneraios."
        "Your drafts are precise, compliant with Indian Standard law, and written in plain yet formal legal language."
    ),
    llm =llm,
    tools=[],
    verbose=True
)