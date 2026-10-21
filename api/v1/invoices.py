# Copyright (c) 2026 MOHAMMAD SUBHAN PASHA
from fastapi import APIRouter
router = APIRouter()
@router.get("/parse")
def parse_invoice():
    return {"inventor": "MOHAMMAD SUBHAN PASHA", "cost": "$0 vs $2.67M", "rbi": True}
