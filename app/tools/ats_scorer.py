# app/tools/ats_scorer.py

def calculate_ats_score(resume_text: str, job_desc: str):
    resume_words = set(resume_text.lower().split())
    job_words = set(job_desc.lower().split())

    match = resume_words.intersection(job_words)
    score = (len(match) / len(job_words)) * 100 if job_words else 0

    return round(score, 2)