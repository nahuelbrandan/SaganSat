"""Custom error reporting functions."""

from fastapi import Request
from fastapi.responses import JSONResponse
from starlette import status

from saganSat.exceptions import EmptyTasksException


def empty_tasks_handler(request: Request, exc: EmptyTasksException):
    """Use HTTP Exception raiser to report an empty tasks."""
    detail = "No list of Tasks to create was provided."
    status_code = status.HTTP_400_BAD_REQUEST

    return JSONResponse(
        status_code=status_code,
        content={"detail": detail},
    )
