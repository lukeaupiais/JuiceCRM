from pydantic import BaseModel
from typing import Optional

class OpportunityBase(BaseModel):
    name: str
    description: Optional[str] = None
    amount: float
    status: str

class OpportunityCreate(OpportunityBase):
    pass

class OpportunityUpdate(OpportunityBase):
    name: Optional[str] = None
    description: Optional[str] = None
    amount: Optional[float] = None
    status: Optional[str] = None

class Opportunity(OpportunityBase):
    id: int

    class Config:
        orm_mode = True


class TicketBase(BaseModel):
    subject: str
    description: str
    status: str
    priority: str


class TicketCreate(TicketBase):
    pass


class Ticket(TicketBase):
    id: int

    class Config:
        orm_mode = True