import requests

from config import BASE_URL, TOKEN


def test_create_project():
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }

    response = requests.post(
        f"{BASE_URL}/projects",
        headers=headers,
        json={"title": "Test project"}
    )

    assert response.status_code == 201
    assert response.json()["id"]


def test_get_project():
    headers = {
        "Authorization": f"Bearer {TOKEN}"
    }

    create_response = requests.post(
        f"{BASE_URL}/projects",
        headers=headers,
        json={"title": "Get test project"}
    )

    assert create_response.status_code == 201

    project_id = create_response.json()["id"]

    response = requests.get(
        f"{BASE_URL}/projects/{project_id}",
        headers=headers
    )

    assert response.status_code == 200
    assert response.json()["title"] == "Get test project"


def test_update_project():
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }

    create_response = requests.post(
        f"{BASE_URL}/projects",
        headers=headers,
        json={"title": "Old project title"}
    )

    assert create_response.status_code == 201

    project_id = create_response.json()["id"]

    response = requests.put(
        f"{BASE_URL}/projects/{project_id}",
        headers=headers,
        json={"title": "Updated project title"}
    )

    assert response.status_code == 200

    get_response = requests.get(
        f"{BASE_URL}/projects/{project_id}",
        headers=headers
    )

    assert get_response.status_code == 200
    assert get_response.json()["title"] == "Updated project title"


def test_create_project_without_title():
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }

    response = requests.post(
        f"{BASE_URL}/projects",
        headers=headers,
        json={}
    )

    assert response.status_code == 400
    assert "title" in response.text


def test_get_project_with_invalid_id():
    headers = {
        "Authorization": f"Bearer {TOKEN}"
    }

    invalid_project_id = "00000000-0000-0000-0000-000000000000"

    response = requests.get(
        f"{BASE_URL}/projects/{invalid_project_id}",
        headers=headers
    )

    assert response.status_code == 404
    assert "not found" in response.text.lower()


def test_update_project_with_invalid_id():
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }

    invalid_project_id = "00000000-0000-0000-0000-000000000000"

    response = requests.put(
        f"{BASE_URL}/projects/{invalid_project_id}",
        headers=headers,
        json={"title": "Updated project"},
        timeout=10
    )

    assert response.status_code == 404
    assert "not found" in response.text.lower()
