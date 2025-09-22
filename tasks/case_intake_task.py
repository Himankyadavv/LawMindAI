# CASE INTAKE TASK 

#import libraries 
from crewai import Task 
from agents.case_intake_agent import intake_agent

case_intake_task = Task(
    agent=intake_agent,
    description=(
        "The user has submitted the following legal query:\n\n"
        "{user_input}\n\n"
        "Your job is to interpret it, identify the legal issue, classify the legal domain" 
        "(e.g., civil, criminal, labor), and return a structured json with: "
        "`case type`, `legal domain`, `summary`, 'relevant entities`, 'jurisdiction` (if any)."
    ),
    expected_output=(
        "```json\n"
        "{\n"
        " \"case Type\": \"Wrongful Termination\",\n"
        " \"legal Domain\": \"Labor Law\",\n"
        " \"summary\": \"The user reports being fired after refusing to work overtime unpaid\",\n"
        " \"relevant entities\":[\"user\",\"employee\"],\n",
        " \"jurisdiction\":\"India\"\n"
        "}\n"
        "```"
    ),


)