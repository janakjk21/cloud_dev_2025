from fastapi import APIRouter, HTTPException, BackgroundTasks
from uuid import uuid4
from schemas.jobs import JobCreate, JobStatus  # Correct import from schemas folder

router = APIRouter()

# Mock data stores
mock_user = {"id": 1, "credits": 10}
jobs_store = {}

# Background task to simulate job processing
def process_job(job_id: str):
    import time
    time.sleep(5)  # Simulate processing time
    jobs_store[job_id]["status"] = "completed"
    jobs_store[job_id]["output"] = "Short summary."

@router.post("/submit", response_model=dict)
def submit_job(job: JobCreate, background_tasks: BackgroundTasks):
    """
    Submit a job for processing.
    """
    if mock_user["credits"] <= 0:
        raise HTTPException(status_code=400, detail="Insufficient credits")

    # Deduct 1 credit
    mock_user["credits"] -= 1

    # Create a job ID and store the job
    job_id = str(uuid4())
    jobs_store[job_id] = {"status": "queued", "output": None}

    # Queue the job for background processing
    background_tasks.add_task(process_job, job_id)

    return {"job_id": job_id}

@router.get("/{job_id}/status", response_model=JobStatus)
def check_job_status(job_id: str):
    """
    Check the status of a submitted job.
    """
    job = jobs_store.get(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    return {"status": job["status"], "output": job["output"]}