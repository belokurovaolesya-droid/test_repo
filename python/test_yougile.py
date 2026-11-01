import requests

BASE_URL = "https://ru.yougile.com/api-v2"
API_KEY = "R-a-plQgwVlEViSw7O1IuWZxuJ1BTMjukw0ZDbG7xoh1SQRbVVt611nwoWVXHbtV" 
COLUMN_ID = "a9208230-49b8-46a5-b554-717a5e5e532f" 

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def test_full_task_lifecycle():
    payload_create = {
        "title": "Автотест: Задача для проверки",
        "columnId": COLUMN_ID
    }
    response_create = requests.post(f"{BASE_URL}/tasks", json=payload_create, headers=headers)
    assert response_create.status_code == 201
    
    task_id = response_create.json().get("id")
    assert task_id is not None

    payload_update = {"title": "Автотест: ОБНОВЛЕННАЯ задача"}
    response_update = requests.put(f"{BASE_URL}/tasks/{task_id}", json=payload_update, headers=headers)
    assert response_update.status_code == 200

    response_get_single = requests.get(f"{BASE_URL}/tasks/{task_id}", headers=headers)
    assert response_get_single.status_code == 200
    
    updated_title = response_get_single.json().get("title")
    if isinstance(updated_title, str):
        assert updated_title == "Автотест: ОБНОВЛЕННАЯ задача"

def test_create_task_without_auth():
    payload = {"title": "Хакерская задача", "columnId": COLUMN_ID}
    response = requests.post(f"{BASE_URL}/tasks", json=payload, headers={"Content-Type": "application/json"})
    assert response.status_code == 401

def test_create_task_invalid_column():
    payload = {"title": "Задача в никуда", "columnId": "00000000-0000-0000-0000-000000000000"}
    response = requests.post(f"{BASE_URL}/tasks", json=payload, headers=headers)
    assert response.status_code in [400, 404]