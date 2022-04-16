"""Endpoints REST of the API."""
from typing import List

from fastapi import Body, APIRouter
from starlette import status
from starlette.requests import Request
from starlette.responses import FileResponse

from saganSat import settings
from saganSat.models import Task, SystemDetails, TaskResponse

router = APIRouter()


@router.get(
    path="/",
    tags=['System'],
    response_model=SystemDetails
)
def get_system_info(
    request: Request,
):
    """Get system details."""
    base_url = str(request.base_url).strip("/")
    docs = f"{base_url}/docs"

    response = SystemDetails(
        title=settings.TITLE,
        description=f'{settings.DESCRIPTION} For more information see the /docs endpoint.',
        version=settings.VERSION,
        docs=docs,
    )

    return response


@router.put(
    path="/tasks",
    tags=['Task'],
    response_model=TaskResponse,
    status_code=status.HTTP_201_CREATED,
)
def process_tasks(
    request: Request,
    tasks: List[Task] = Body(
        ...,
        title="Task List",
        description="List of tasks to run in a satellite.",
        example=[
            {
                "name": "Pictures",
                "resources": [1, 5],
                "payoff": 10,
            },
            {
                "name": "Maintenance",
                "resources": [1, 2],
                "payoff": 1,
            },
            {
                "name": "Proofs",
                "resources": [5, 6],
                "payoff": 1,
            },
            {
                "name": "Files",
                "resources": [1, 6],
                "payoff": 0.1,
            }
        ]
    ),
):
    """Schedule and tasking the tasks."""
    # TODO process the list of tasks.

    # TODO result of the process

    response = TaskResponse(
        tasks_sended_to_the_satellite_1=['asd'],
        tasks_sended_to_the_satellite_2=['qwe', 'rty'],
        responses_of_the_satellite_1=["The 'asd' task was successfully processed."],
        responses_of_the_satellite_2=["The 'qwe' task was successfully processed.",
                                      "The 'rty' task was failed processed."],
    )
    return response


@router.get(path='/favicon.ico', include_in_schema=False)
def favicon():
    """Get the favicon of the website.

    This is requested in case that access from the navigator.
    """
    return FileResponse('./resources/img/favicon.ico')
