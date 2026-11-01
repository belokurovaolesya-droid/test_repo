import pytest
import requests
import allure
from config import Config

pytestmark = pytest.mark.api

@allure.story("API")
@allure.title("Создание задачи")
def test_create_task(base_url: str, api_headers: dict) -> None:
    payload = {"title": "API Task 1", "columnId": Config.COLUMN_ID}
    with allure.step("Отправка POST запроса на создание задачи"):
        response = requests.post(f"{base_url}/tasks", json=payload, headers=api_headers)
    with allure.step("Проверка статус-кода 201"):
        assert response.status_code == 201

@allure.story("API")
@allure.title("Получение списка задач")
def test_get_tasks(base_url: str, api_headers: dict) -> None:
    with allure.step("Отправка GET запроса"):
        response = requests.get(f"{base_url}/tasks", headers=api_headers)
    with allure.step("Проверка статус-кода 200"):
        assert response.status_code == 200

@allure.story("API")
@allure.title("Обновление задачи")
def test_update_task(base_url: str, api_headers: dict) -> None:
    with allure.step("Создание задачи для обновления"):
        payload = {"title": "Task to update", "columnId": Config.COLUMN_ID}
        create_resp = requests.post(f"{base_url}/tasks", json=payload, headers=api_headers)
        task_id = create_resp.json().get("id")
    with allure.step("Отправка PUT запроса на обновление"):
        update_payload = {"title": "Updated Task"}
        update_resp = requests.put(f"{base_url}/tasks/{task_id}", json=update_payload, headers=api_headers)
    with allure.step("Проверка статус-кода 200"):
        assert update_resp.status_code == 200

@allure.story("API")
@allure.title("Создание задачи без авторизации")
def test_create_task_without_auth(base_url: str) -> None:
    with allure.step("Отправка POST запроса без токена"):
        payload = {"title": "No Auth", "columnId": Config.COLUMN_ID}
        response = requests.post(f"{base_url}/tasks", json=payload, headers={"Content-Type": "application/json"})
    with allure.step("Проверка статус-кода 401"):
        assert response.status_code == 401

@allure.story("API")
@allure.title("Создание задачи с невалидным ID колонки")
def test_create_task_invalid_column(base_url: str, api_headers: dict) -> None:
    with allure.step("Отправка POST запроса с неверным columnId"):
        payload = {"title": "Invalid", "columnId": "00000000-0000-0000-0000-000000000000"}
        response = requests.post(f"{base_url}/tasks", json=payload, headers=api_headers)
    with allure.step("Проверка статус-кода 400 или 404"):
        assert response.status_code in [400, 404]