from fastapi import FastAPI, HTTPException
from sqlmodel import SQLModel, Field, Session, create_engine, select
from typing import List
from pydantic import BaseModel
import os

# 1) Define your ORM model
class Attendance(SQLModel, table=True):
    id:    int    = Field(default=None, primary_key=True)
    PersonId:   str
    PersonName: str
    Timestamp:  int
    DeviceIp:   str
    DeviceName: str
    State:      int
    Method:     int
    # add any other fields you posted…

# 2) Create (or open) your SQLite database file
sqlite_file = os.path.join(os.path.dirname(__file__), "attendance.db")
engine = create_engine(f"sqlite:///{sqlite_file}", echo=False)

# 3) Create the table if it doesn’t already exist
SQLModel.metadata.create_all(engine)

app = FastAPI()


@app.post("/upload-log", status_code=201)
async def upload_log(record: Attendance):
    # record comes in as JSON matching Attendance fields
    with Session(engine) as sess:
        sess.add(record)
        sess.commit()
        sess.refresh(record)
    return {"status": "ok", "id": record.id}


@app.get("/attendance", response_model=List[Attendance])
def get_attendance():
    with Session(engine) as sess:
        statement = select(Attendance).order_by(Attendance.Timestamp)
        results = sess.exec(statement).all()
    return results
