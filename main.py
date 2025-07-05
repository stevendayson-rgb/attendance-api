from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Attendance API is live!"}

@app.post("/upload-log")
async def upload_log(request: Request):
    data = await request.json()
    print("Received log:", data)
    return {"status": "success", "data": data}
