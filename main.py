from fastapi import FastAPI, Request
from typing import List, Dict

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Attendance API is live!"}

# ← ADD THIS
@app.get("/attendance", response_model=List[Dict])
def list_attendance():
    # TODO: replace this stub with real data fetch from your DB or in-memory store
    return []

@app.post("/upload-log")
async def upload_log(request: Request):
    data = await request.json()
    print("Received log:", data)
    # TODO: insert into your database here
    return {"status": "success", "data": data}

