# Crew.py

# import libraries 

from crewai import Crew
from agents.case_intake_agent import intake_agent
from agents.ipc_section_agent import ipc_section_agent
from agents.legal_precedents_agent import precendent_agent
from agents.legal_drafter_agent import legal_agent
from tasks.case_intake_task import case_intake_task
from tasks.ipc_section_task import ipc_section_task
from tasks.legal_precedent_task import legal_precedent_task
from tasks.legal_drafter_task import legat_drafter_task

legat_assistant_crew = Crew(
    agents=[intake_agent, ipc_section_agent, precendent_agent, legal_agent],
    tasks=[case_intake_task, ipc_section_task,legal_precedent_task, legat_drafter_task ],
    verbose=True
) 
