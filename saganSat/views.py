"""Endpoints REST of the API."""
from typing import List

from fastapi import Body, APIRouter
from starlette import status
from starlette.requests import Request
from starlette.responses import FileResponse

from saganSat import settings
from saganSat.models import Task, SystemDetails, TaskResponse
from saganSat.utils import process_the_tasks_to_group_to_maximize_the_payload

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
    tasks_grouped = process_the_tasks_to_group_to_maximize_the_payload(tasks)

    # for test
    for i, conn_pipe in enumerate(request.app.satellites_pipes):
        conn_pipe.send([tasks[i]])

    responses = []
    for i, conn_pipe in enumerate(request.app.satellites_pipes):
        responses.extend(conn_pipe.recv())

    print(f'ALL RESPONSES: {responses}')

    response = TaskResponse(details=responses)
    return response


@router.get(path='/favicon.ico', include_in_schema=False)
def favicon():
    """Get the favicon of the website.

    This is requested in case that access from the navigator.
    """
    return FileResponse('./resources/img/favicon.ico')
