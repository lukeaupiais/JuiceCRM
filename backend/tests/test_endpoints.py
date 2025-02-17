from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.app.main import app, get_db
from backend.app.database import database
from backend.app.models import models
import pytest

SQLALCHEMY_DATABASE_URL = "sqlite:///./test_test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture()
def test_db():
    Base = models.Base
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_create_opportunity(test_db):
    response = client.post(
        "/opportunities/",
        json={"name": "Test Opportunity", "amount": 1000.0, "status": "Open", "description": "Test Description"},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "Test Opportunity"
    assert data["amount"] == 1000.0
    assert data["status"] == "Open"
    assert "id" in data

def test_read_opportunities(test_db):
    # First, create an opportunity to ensure there's something to read
    client.post(
        "/opportunities/",
        json={"name": "Test Opportunity", "amount": 1000.0, "status": "Open", "description": "abc"},
    )
    response = client.get("/opportunities/")
    assert response.status_code == 200, response.text
    data = response.json()
    assert len(data) > 0  # Check that the list is not empty
    assert data[0]["name"] == "Test Opportunity"  # Check the content of the first item

def test_read_opportunity(test_db):
    # Create an opportunity
    response = client.post(
        "/opportunities/",
        json={"name": "Test Opportunity", "amount": 1000.0, "status": "Open", "description":"abc"},
    )
    opportunity_id = response.json()["id"]

    # Read the created opportunity
    response = client.get(f"/opportunities/{opportunity_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "Test Opportunity"
    assert data["id"] == opportunity_id

def test_update_opportunity(test_db):
    # Create
    response = client.post(
        "/opportunities/",
        json={"name": "Test Opportunity", "amount": 1000.0, "status": "Open", "description":"abc"},
    )
    opportunity_id = response.json()["id"]
    #Update
    response = client.put(
        f"/opportunities/{opportunity_id}",
        json={"name": "Updated Opportunity", "amount": 1200.0},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "Updated Opportunity"
    assert data["amount"] == 1200.0

    # Check that it was actually updated in the database
    response = client.get(f"/opportunities/{opportunity_id}")
    data = response.json()
    assert data["name"] == "Updated Opportunity"
    assert data["amount"] == 1200.0

def test_delete_opportunity(test_db):
    # Create
    response = client.post(
        "/opportunities/",
        json={"name": "Test Opportunity", "amount": 1000.0, "status": "Open", "description":"abc"},
    )
    opportunity_id = response.json()["id"]

    # Delete
    response = client.delete(f"/opportunities/{opportunity_id}")
    assert response.status_code == 200, response.text
    assert response.json() == {"message": "Opportunity deleted"}

    # Check that it's no longer accessible
    response = client.get(f"/opportunities/{opportunity_id}")
    assert response.status_code == 404, response.text