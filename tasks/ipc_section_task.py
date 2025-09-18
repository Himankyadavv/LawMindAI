# IPC Section Task 

# import libraries 
from crewai import Task
from agents.ipc_section_agent import ipc_section_agent
from tasks.case_intake_task import case_intake_task

# create task for finding ipc section 
ipc_section_task = Task(
    agent=ipc_section_agent,
    description=(
        "You are provided with sturctured legal context generated from the previous task.\n\n"
        "Your job is to find and retreive the most relevant sections from the Indian Penal Code(IPC)"
        "that apply to this legal issue. Use your tool to search and extract the top 3 most relevant IPC Sections"
        "Return the result with clean JSON format with the following fields: \n\n"
        "- `section`\n"
        "- `section_title`\n"
        "- `chapter`\n"
        "- `chatper_title`\n"
        "- `content`\n"
    ),
    expected_output=(
        "```json \n"
        "{\n"
        "   {\n"
            "\"section\": \"Wrongful Termination\",\n"
            "\"section_title\": \"Labor Law\",\n"
            "\"chapter\": \"The user reports being fired after refusing to work overtime unpaid\",\n"
            "\"chapter_title\":[\"user\"employee\"],n",
            "\"content\":\"India\",\n"
            "},\n"
        "{ ... },\n"
        "{ ... }\n"
        "}\n"
        "```"
    )
)