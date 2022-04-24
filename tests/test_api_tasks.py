"""Test API request.

This tests works as an integration tests, testing the request of the client and the response that this obtains.

There are supposed to be 2 satellites, that is the default value defined in SETTINGS.
"""
import json
import re
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_no_body():
    """The request body is required in tasks endpoint."""
    response = client.post("/tasks")

    assert response.status_code == 422
    assert list(response.json().keys()) == ["detail"]

    expected_detail = [
        {
            'loc': ['body'],
            'msg': 'field required',
            'type': 'value_error.missing'
        }
    ]
    assert response.json()['detail'] == expected_detail


def test_body_empty_list_of_tasks():
    """Test post a task, with an empty list of tasks as body."""
    payload = json.dumps([])
    response = client.post("/tasks", data=payload)

    assert response.status_code == 400
    assert list(response.json().keys()) == ["detail"]

    expected_detail = 'No list of Tasks to create was provided.'
    assert response.json()['detail'] == expected_detail


def test_only_one_task():
    """Test post tasks, with a list of tasks with only one task."""
    payload = json.dumps(
        [
            {
                "name": "Pictures",
                "resources": [1, 5],
                "payoff": 10
            }
        ]
    )
    response = client.post("/tasks", data=payload)

    assert response.status_code == 201
    assert list(response.json().keys()) == ["detail"]

    expected_detail = [
        "^The task 'Pictures' was (successful|failed), by the Satellite Sat-0.$"
    ]

    resp_detail = response.json()['detail']

    assert len(resp_detail) == len(expected_detail)

    for i, exp in enumerate(expected_detail):
        assert re.match(exp, resp_detail[i])


def test_two_tasks_that_not_have_resources_in_common():
    """Test post tasks, with a list of two tasks, that not have resources in common."""
    payload = json.dumps(
        [
            {
                "name": "Pictures",
                "resources": [1, 5],
                "payoff": 10
            },
            {
                "name": "Maintenance",
                "resources": [2, 3],
                "payoff": 1
            }
        ]
    )
    response = client.post("/tasks", data=payload)

    assert response.status_code == 201
    assert list(response.json().keys()) == ["detail"]

    expected_detail = [
        "^The task 'Pictures' was (successful|failed), by the Satellite Sat-0.$",
        "^The task 'Maintenance' was (successful|failed), by the Satellite Sat-1.$"
    ]

    resp_detail = response.json()['detail']

    assert len(resp_detail) == len(expected_detail)

    for i, exp in enumerate(expected_detail):
        assert re.match(exp, resp_detail[i])


def test_two_tasks_that_have_a_resource_in_common():
    """Test post tasks, with a list of two tasks, that have a resource in common."""
    payload = json.dumps(
        [
            {
                "name": "Pictures",
                "resources": [1, 5],
                "payoff": 10
            },
            {
                "name": "Maintenance",
                "resources": [1, 3],
                "payoff": 1
            }
        ]
    )
    response = client.post("/tasks", data=payload)

    assert response.status_code == 201
    assert list(response.json().keys()) == ["detail"]

    expected_detail = [
        "^The task 'Pictures' was (successful|failed), by the Satellite Sat-0.$",
        "^The task 'Maintenance' was (successful|failed), by the Satellite Sat-1.$"
    ]

    resp_detail = response.json()['detail']

    assert len(resp_detail) == len(expected_detail)

    for i, exp in enumerate(expected_detail):
        assert re.match(exp, resp_detail[i])


def test_nominal():
    """Test post tasks, nominal case."""
    payload = json.dumps(
        [
            {
                "name": "Pictures",
                "resources": [1, 5],
                "payoff": 10
            },
            {
                "name": "Maintenance",
                "resources": [1, 3],
                "payoff": 1
            },
            {
                "name": "Proofs",
                "resources": [5, 6],
                "payoff": 1
            },
            {
                "name": "Files",
                "resources": [1, 6],
                "payoff": 0.1
            }
        ]
    )
    response = client.post("/tasks", data=payload)

    assert response.status_code == 201
    assert list(response.json().keys()) == ["detail"]

    expected_detail = [
        r"^The task 'Pictures' was (successful|failed), by the Satellite Sat-0.$",
        r"^The task 'Maintenance' was (successful|failed), by the Satellite Sat-1.$",
        r"^The task 'Proofs' was (successful|failed), by the Satellite Sat-1.$"
    ]

    resp_detail = response.json()['detail']

    assert len(resp_detail) == len(expected_detail)

    for i, exp in enumerate(expected_detail):
        assert re.match(exp, resp_detail[i])
