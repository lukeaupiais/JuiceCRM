from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import database
from .models import models
from .schemas import schemas
from typing import List
import json

app = FastAPI()

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/opportunities/", response_model=schemas.Opportunity)
def create_opportunity(opportunity: schemas.OpportunityCreate, db: Session = Depends(get_db)):
    db_opportunity = models.Opportunity(**opportunity.dict())
    db.add(db_opportunity)
    db.commit()
    db.refresh(db_opportunity)
    return db_opportunity

@app.get("/opportunities/", response_model=List[schemas.Opportunity])
def read_opportunities(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    opportunities = db.query(models.Opportunity).offset(skip).limit(limit).all()
    return opportunities

@app.get("/opportunities/{opportunity_id}", response_model=schemas.Opportunity)
def read_opportunity(opportunity_id: int, db: Session = Depends(get_db)):
    db_opportunity = db.query(models.Opportunity).filter(models.Opportunity.id == opportunity_id).first()
    if db_opportunity is None:
        raise HTTPException(status_code=404, detail="Opportunity not found")
    return db_opportunity

@app.put("/opportunities/{opportunity_id}", response_model=schemas.Opportunity)
def update_opportunity(opportunity_id: int, opportunity: schemas.OpportunityUpdate, db: Session = Depends(get_db)):
    db_opportunity = db.query(models.Opportunity).filter(models.Opportunity.id == opportunity_id).first()
    if db_opportunity is None:
        raise HTTPException(status_code=404, detail="Opportunity not found")

    for key, value in opportunity.dict(exclude_unset=True).items():
        setattr(db_opportunity, key, value)

    db.commit()
    db.refresh(db_opportunity)
    return db_opportunity

@app.delete("/opportunities/{opportunity_id}")
def delete_opportunity(opportunity_id: int, db: Session = Depends(get_db)):
    db_opportunity = db.query(models.Opportunity).filter(models.Opportunity.id == opportunity_id).first()
    if db_opportunity is None:
        raise HTTPException(status_code=404, detail="Opportunity not found")
    db.delete(db_opportunity)
    db.commit()
    return {"message": "Opportunity deleted"}

@app.post("/tickets/")
def create_ticket():
   raise HTTPException(status_code=501, detail="Not Implemented")

@app.get("/tickets/")
def read_tickets():
    raise HTTPException(status_code=501, detail="Not Implemented")

@app.get("/tickets/{ticket_id}")
def read_ticket():
    raise HTTPException(status_code=501, detail="Not Implemented")

@app.put("/tickets/{ticket_id}")
def update_ticket():
    raise HTTPException(status_code=501, detail="Not Implemented")

@app.delete("/tickets/{ticket_id}")
def delete_ticket():
    raise HTTPException(status_code=501, detail="Not Implemented")