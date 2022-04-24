"""Data Models."""
from typing import List

from pydantic import BaseModel


class Task(BaseModel):
    """Task model, that receive the Ground Station to run in the Satellites."""
    name: str
    resources: List[int]
    payoff: float

    class Config:
        """Extras configs."""
        schema_extra = {
            "example": {
                "name": "Pictures",
                "resources": [1, 5],
                "payoff": 10,
            }
        }


class TaskResult(BaseModel):
    """Task Result model, response to the client of the operation."""
    detail: List[str]

    class Config:
        """Extras configs."""
        schema_extra = {
            "example": {
                "detail": [
                    "The task 'Pictures' was failed, by the Satellite Sat-0.",
                    "The task 'Maintenance' was successfully, by the Satellite Sat-1."
                ]
            }
        }


class SystemDetails(BaseModel):
    """System detail model."""
    title: str
    description: str
    version: str
    docs: str

    class Config:
        """Extras configs."""
        schema_extra = {
            "example": {
                "title": "SaganSat",
                "description": "A description of the system.",
                "version": '0.0.1',
                "docs": 'http://localhost:8000/docs',
            }
        }
