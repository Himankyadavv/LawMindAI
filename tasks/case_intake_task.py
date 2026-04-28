# CASE INTAKE TASK 

#import libraries 
from crewai import Task 
from Agents.case_intake_agent import intake_agent

expected_output = """```json
{
  "case_type": "Wrongful Termination",
  "legal_domain": "Labor Law",
  "summary": "The user reports being fired after refusing to work unpaid overtime.",
  "relevant_entities": ["user", "employer"],
  "jurisdiction": "India"
}
```"""
    
print(type(expected_output))
case_intake_task = Task(
    agent=intake_agent,
    description=(
        "The user has submitted the following legal query:\n\n"
        "{user_input}\n\n"
        "Your job is to interpret it, identify the legal issue, classify the legal domain" 
        "(e.g., civil, criminal, labor), and return a structured json with: "
        "`case type`, `legal domain`, `summary`, `relevant entities`, `jurisdiction` (if any)."
    ),
    expected_output=expected_output
    
)