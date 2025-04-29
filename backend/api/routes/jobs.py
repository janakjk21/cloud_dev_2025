import os
import asyncio
import requests
from fastapi import APIRouter, HTTPException
from schemas.jobs import JobCreate, JobStatusResponse
from database import db
from uuid import uuid4
from config import DEEPSEEK_API_KEY, DEEPSEEK_API_URL

router = APIRouter(tags=["Jobs"])

# In-memory fake database for jobs
jobs_store = {}

@router.post("/submit")
async def submit_job(job: JobCreate):
    user = db.get_user()

    if user["credits"] <= 0:
        raise HTTPException(status_code=403, detail="Insufficient credits.")

    # Deduct one credit
    db.update_user_credits(user["username"], user["credits"] - 1)

    # Create job record
    job_id = str(uuid4())
    jobs_store[job_id] = {
        "task_type": job.task_type,
        "input_data": job.input_data,
        "status": "queued",
        "output": None
    }

    # Trigger background task to process the job
    asyncio.create_task(call_deepseek_api(job_id, job.input_data))

    return {"job_id": job_id}

async def call_deepseek_api(job_id: str, user_input: str):
    try:
        jobs_store[job_id]["status"] = "in_progress"

        headers = {
            "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "deepseek-chat",   # Check your DeepSeek model name
            "messages": [{"role": "user", "content": user_input}],
            "temperature": 0.7,
            "max_tokens": 1024
        }

        response = requests.post(DEEPSEEK_API_URL, headers=headers, json=payload)

        if response.status_code == 200:
            result = response.json()["choices"][0]["message"]["content"]
            jobs_store[job_id]["output"] = result
            jobs_store[job_id]["status"] = "completed"
        else:
            jobs_store[job_id]["output"] = f"Error: {response.text}"
            jobs_store[job_id]["status"] = "failed"

    except Exception as e:
        jobs_store[job_id]["output"] = str(e)
        jobs_store[job_id]["status"] = "failed"

@router.get("/{job_id}/status", response_model=JobStatusResponse)
async def check_job_status(job_id: str):
    job = jobs_store.get(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found.")
    return JobStatusResponse(
        status=job["status"],
        output=job["output"]
    )
