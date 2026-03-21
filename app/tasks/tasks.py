from crewai import Task

def get_tasks(agents, resume_text, job_desc):

    return [
        Task(
            description=f"Analyze this resume:\n{resume_text}",
            agent=agents["resume"],
            expected_output="Structured summary of skills, experience, and key strengths"
        ),
        Task(
            description=f"Analyze this job description:\n{job_desc}",
            agent=agents["job"],
            expected_output="Structured job breakdown including skills, responsibilities, and keywords"
        ),
        Task(
            description="Compare resume and job description and find gaps",
            agent=agents["matcher"],
            expected_output="List of matching skills, missing skills, and overall fit"
        ),
        Task(
            description="Improve resume based on job description",
            agent=agents["optimizer"],
            expected_output="Optimized resume with improvements and ATS alignment"
        ),
        Task(
            description="Generate a tailored cover letter",
            agent=agents["cover"],
            expected_output="Professional, personalized cover letter"
        ),
        # Task(
        #     description="Generate interview questions and answers",
        #     agent=agents["interview"],
        #     expected_output="List of categorized interview questions with answers"
        # )
    ]