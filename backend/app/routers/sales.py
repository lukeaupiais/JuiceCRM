from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from ...database import database
from ... import models, schemas

router = APIRouter(
    prefix="/sales",
    tags=["Sales"],
)

# Create a new sales opportunity
@router.post("/opportunities/", response_model=schemas.Opportunity)
def create_opportunity(opportunity: schemas.OpportunityCreate, db: Session = Depends(database.get_db)):
    db_opportunity = models.Opportunity(**opportunity.dict())
    db.add(db_opportunity)
    db.commit()
    db.refresh(db_opportunity)
    return db_opportunity

# Get opportunity by ID
@router.get(