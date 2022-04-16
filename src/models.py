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


class TaskResponse(BaseModel):
    """Task Response model, response to the client of the operation."""
    tasks_sended_to_the_satellite_1: List[str]
    tasks_sended_to_the_satellite_2: List[str]
    responses_of_the_satellite_1: List[str]
    responses_of_the_satellite_2: List[str]

    class Config:
        """Extras configs."""
        schema_extra = {
            "example": {
                "tasks_sended_to_the_satellite_1": ["Pictures"],
                "tasks_sended_to_the_satellite_2": ["Maintenance", "Proofs"],
                "responses_of_the_satellite_1": ["The 'Pictures' task was successfully processed."],
                "responses_of_the_satellite_2": ["The 'Maintenance' task was successfully processed.",
                                                 "The 'Proofs' task was failed processed."]
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
