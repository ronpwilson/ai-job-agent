from crewai import Crew

from app.agents.resume_agent import get_resume_agent
from app.agents.job_agent import get_job_agent
from app.agents.matcher_agent import get_matcher_agent
from app.agents.optimizer_agent import get_optimizer_agent
from app.agents.cover_letter_agent import get_cover_agent
from app.agents.interview_agent import get_interview_agent

from app.tasks.tasks import get_tasks


def run_crew(resume_text, job_desc):

    agents = {
        "resume": get_resume_agent(),
        "job": get_job_agent(),
        "matcher": get_matcher_agent(),
        "optimizer": get_optimizer_agent(),
        "cover": get_cover_agent(),
        # "interview": get_interview_agent()
    }

    tasks = get_tasks(agents, resume_text, job_desc)

    crew = Crew(
        agents=list(agents.values()),
        tasks=tasks,
        verbose=True
    )

    return crew.kickoff()