from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/hello")
async def hello_world():
    return JSONResponse(content={"message": "Hello from FastAPI on Vercel!"})
