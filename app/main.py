from fastapi import FastAPI
from pydantic import BaseModel, Field
from app.service import analyze_risk

app = FastAPI()


class RiskRequest(BaseModel):
    summary: str = Field(..., min_length=1)


@app.get("/")
def health():
    return {"status": "ok"}


@app.post("/analyze-risk")
def analyze(request: RiskRequest):
    return analyze_risk(request.summary)
