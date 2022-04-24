"""Endpoints REST of the API."""
from typing import List

from fastapi import Body, APIRouter
from fastapi.openapi.docs import get_swagger_ui_html
from starlette import status
from starlette.requests import Request
from starlette.responses import FileResponse

from saganSat import settings
from saganSat.exceptions import EmptyTasksException
from saganSat.ground_station import GroundStation
from saganSat.logs import logger
from saganSat.models import Task, SystemDetails, TaskResult

router = APIRouter()


@router.get(
    path="/",
    tags=['System'],
    response_model=SystemDetails
)
def get_system_info(
    request: Request,
):
    """Get system detail."""
    base_url = str(request.base_url).strip("/")
    docs = f"{base_url}/docs"

    response = SystemDetails(
        title=settings.TITLE,
        description=f'{settings.DESCRIPTION} For more information see the /docs endpoint.',
        version=settings.VERSION,
        docs=docs,
    )

    return response


@router.post(
    path="/tasks",
    tags=['Task'],
    response_model=TaskResult,
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
    """The Ground Station get a list of Tasks, manages them and assign them to the respective Satellites to be run.

    ### Args:

    * tasks (List[Task]): list of task to manage per the Ground Station y expect to be run by the Satellites.

    ### Returns:

    * List[str]: obtained result for each runner tasks. The options are:
        * Successfully run by the Satellite X.
        * Failure run by the Satellite X.

    ### Task:

    A Task is composed by:

    * **Name:** functions as an ID of the Task
    * **Resources:** list of Resource IDs that require the Task to run
    * **Payoff:** The benefit generated by executing the task.

    ### Constraint:

    * The resources work as an **exclusive locks**,
    therefore, in the same pass, each of the satellites
    can only be assigned tasks that do not have repeated resources.
    * The assignment of tasks must **maximize the payoff**.
    """

    if not tasks:
        raise EmptyTasksException()

    gs = GroundStation(
        satellites_pipes=request.app.satellites_pipes
    )

    gs.group_tasks_to_run_per_satellite(tasks)
    gs.send_grouped_tasks_to_the_satellites()
    responses = gs.get_responses_of_satellites()

    logger.info(f'All responses obtained from satellites: {responses}')
    response = TaskResult(detail=responses)
    return response


@router.get(
    path='/favicon.ico',
    include_in_schema=False
)
def favicon():
    """Get the favicon of the website.

    This is requested in case that access from the navigator.
    """
    return FileResponse(settings.LOGO_PATH)


@router.get(
    path="/docs",
    include_in_schema=False
)
def overridden_swagger():
    """Override default endpoint /docs, for custom changes."""
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title=f"{settings.TITLE} - Swagger",
        swagger_favicon_url="/favicon.ico",
    )
