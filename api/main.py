from fastapi import FastAPI, UploadFile, File, Form
import shutil

from app.tools.resume_parser import parse_resume
from app.tools.ats_scorer import calculate_ats_score
from app.crew import run_crew

app = FastAPI()
from dotenv import load_dotenv
load_dotenv()

import os


@app.post("/analyze")
async def analyze(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):
    print("got request")
    file_path = f"temp_{resume.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(resume.file, buffer)

    resume_text = parse_resume(file_path)

    result = run_crew(resume_text, job_description)

    ats_score = calculate_ats_score(resume_text, job_description)

    os.remove(file_path)

    return {
        "ats_score": ats_score,
        "analysis": str(result)
    }