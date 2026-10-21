# Copyright (c) 2026 MOHAMMAD SUBHAN PASHA
from fastapi import FastAPI
app = FastAPI(title="Bharat FinGPT Sovereign OS - MOHAMMAD SUBHAN PASHA")

@app.get("/")
def root():
    return {"inventor": "MOHAMMAD SUBHAN PASHA", "patent": "IN2026/FINGPT-OMNI-SOVEREIGN-OS", "cost": "$0 vs $2.67M", "status": "200 OK"}

@app.get("/health")
def health():
    return {"status": "200 OK", "rbi": True}
