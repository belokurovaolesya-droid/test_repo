import uuid

import requests

from config import BASE_URL, HEADERS


PROJECTS_URL = f"{BASE_URL}/api-v2/projects"


def create_project():
    project_name = f"API test {uuid.uuid4()}"

    response = requests.post(
        PROJECTS_URL,
        headers=HEADERS,
        json={
            "title": project_name,
        },
    )

    return response, project_name


def test_create_project_positive():
    response, project_name = create_project()

    assert response.status_code == 201

    project = response.json()

    assert project["id"]

    project_id = project["id"]

    get_response = requests.get(
        f"{PROJECTS_URL}/{project_id}",
        headers=HEADERS,
    )

    assert get_response.status_code == 200

    project_data = get_response.json()

    assert project_data["title"] == project_name


def test_create_project_negative():
    response = requests.post(
        PROJECTS_URL,
        headers=HEADERS,
        json={},
    )

    assert response.status_code >= 400
    assert "error" in response.json()


def test_get_project_positive():
    create_response, project_name = create_project()

    assert create_response.status_code == 201

    project_id = create_response.json()["id"]

    response = requests.get(
        f"{PROJECTS_URL}/{project_id}",
        headers=HEADERS,
    )

    assert response.status_code == 200

    project = response.json()

    assert project["id"] == project_id
    assert project["title"] == project_name


def test_get_project_negative():
    fake_id = str(uuid.uuid4())

    response = requests.get(
        f"{PROJECTS_URL}/{fake_id}",
        headers=HEADERS,
    )

    assert response.status_code >= 400
    assert "error" in response.json()


def test_update_project_positive():
    create_response, project_name = create_project()

    assert create_response.status_code == 201

    project_id = create_response.json()["id"]
    new_name = f"Updated {project_name}"

    response = requests.put(
        f"{PROJECTS_URL}/{project_id}",
        headers=HEADERS,
        json={
            "title": new_name,
        },
    )

    assert response.status_code == 200

    get_response = requests.get(
        f"{PROJECTS_URL}/{project_id}",
        headers=HEADERS,
    )

    assert get_response.status_code == 200

    project = get_response.json()

    assert project["id"] == project_id
    assert project["title"] == new_name


def test_update_project_negative():
    fake_id = str(uuid.uuid4())

    response = requests.put(
        f"{PROJECTS_URL}/{fake_id}",
        headers=HEADERS,
        json={
            "title": "Invalid project",
        },
    )

    assert response.status_code >= 400
    assert "error" in response.json()
