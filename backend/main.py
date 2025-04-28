from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes.auth import router as auth_router
from api.routes.history import router as history_router
from api.routes.jobs import router as jobs_router
from api.routes.user import router as user_router

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Replace with the frontend's origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Include routers
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(history_router, prefix="/history", tags=["history"])
app.include_router(jobs_router, prefix="/jobs", tags=["jobs"])
app.include_router(user_router, prefix="/user", tags=["user"])  
# Root endpoint

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI app!"}