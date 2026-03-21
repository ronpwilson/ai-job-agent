# app/agents/matcher_agent.py

from crewai import Agent
from app.config import get_llm

def get_matcher_agent():
    return Agent(
        role="Resume Matcher",
        goal="Compare resume with job description and find skill gaps",
        backstory="Expert recruiter matching candidates",
        llm=get_llm(),
        verbose=True
    )