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
    details: List[str]

    class Config:
        """Extras configs."""
        schema_extra = {
            "example": {
                "details": [
                    "The task 'Pictures' was failed, by the Satellite '0'.",
                    "The task 'Maintenance' was successfully done, by the Satellite '1'."
                ]
            }
        }


class SystemDetails(BaseModel):
    """System details model."""
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
