from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from ...database import database
from ... import models, schemas

router = APIRouter(
    prefix="/customer_support",
    tags=["Customer Support"],
)

# Create a new support ticket
@router.post("/tickets/", response_model=schemas.Ticket)
def create_ticket(ticket: schemas.TicketCreate, db: Session = Depends(database.get_db)):
    db_ticket = models.Ticket(**ticket.dict())
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket

# Get ticket by ID
@router.get(