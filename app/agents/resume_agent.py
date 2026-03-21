# app/agents/resume_agent.py

from crewai import Agent
from app.config import get_llm

def get_resume_agent():
    return Agent(
        role="Resume Analyzer",
        goal="Extract key skills and experience from resume",
        backstory="Expert HR with deep understanding of resumes",
        llm=get_llm(),
        verbose=True
    )