# IPC Section Task 

# import libraries 
from crewai import Task
from Agents.ipc_section_agent import ipc_section_agent
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
        "```json\n"
        "[\n"
        "  {\n"
        "    \"section\": \"IPC Section 73\",\n"
        "    \"section_title\": \"Compensation for breach of contract\",\n"
        "    \"chapter\": \"Chapter 6\",\n"
        "    \"chapter_title\": \"Of Breach of Contract\",\n"
        "    \"content\": \"When a contract has been broken...\"\n"
        "  },\n"
        "  { ... },\n"
        "  { ... }\n"
        "]\n"
        "```"
    )
)