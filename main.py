from fastapi import FastAPI, Request
from typing import List, Dict

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Attendance API is live!"}

@app.get("/attendance")
def list_attendance() -> List[Dict]:
    # pull from your in-memory list, DB, etc.
    # for now, just return an empty list or your stub data:
    return []

@app.post("/upload-log")
async def upload_log(request: Request):
    data = await request.json()
    print("Received log:", data)
    # here you’d insert into your DB or in-memory list
    return {"status": "success", "data": data}
