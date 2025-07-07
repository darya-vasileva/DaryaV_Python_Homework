import requests

base_URL = "https://yougile.com/api-v2/"
api_token = ""

headers = {
    'Authorization': f'Bearer {api_token}',
    'Content-Type': 'application/json'
}


# POST - запросы (Создать):


def test_create_project_positive():
    body = {"title": "Домашка_08"}
    response = requests.post(f"{base_URL}projects", json=body, headers=headers)
    assert response.status_code == 201
    data = response.json()
    print(data)
    assert "id" in data

    # удаление проекта
    delete = {'deleted': True}
    requests.put(
        f"{base_URL}projects/{data['id']}", json=delete, headers=headers)


def test_create_project_negative_empty_title():
    body = {}
    response = requests.post(f"{base_URL}projects", json=body, headers=headers)

    assert response.status_code != 201


# PUT - запросы (Изменить):


def test_update_project_positive():

    project_create = {"title": "Старое название"}
    resp_create = requests.post(
        f"{base_URL}projects", json=project_create, headers=headers)

    assert resp_create.status_code == 201
    project = resp_create.json()

    project_id = project["id"]

    new_title = "Новое название"

    project_update = {"title": new_title}

    resp_update = requests.put(
        f"{base_URL}projects/{project_id}",
        json=project_update, headers=headers
        )

    assert resp_update.status_code == 200

    # проверка нового имени через GET
    get_resp = requests.get(
        f"{base_URL}projects/{project_id}", headers=headers)

    get_data = get_resp.json()
    assert get_data["title"] == new_title

    # удаление проекта
    delete = {'deleted': True}
    requests.put(
        f"{base_URL}projects/{project_id}", json=delete, headers=headers)


def test_update_project_negative_invalid_id():
    invalid_id = -1
    body = {"title": "Невалидный ID"}

    response = requests.put(
        f"{base_URL}projects/{invalid_id}", json=body, headers=headers)

    assert response.status_code == 404

# GET - запросы (Получить по ID):


def test_get_project_positive():

    body = {"title": "Домашка_08_Тест"}
    create_resp = requests.post(
        f"{base_URL}projects", json=body, headers=headers)

    assert create_resp.status_code == 201
    project = create_resp.json()

    project_id = project["id"]

    # Получаем проект по id
    get_resp = requests.get(
        f"{base_URL}projects/{project_id}", headers=headers)

    assert get_resp.status_code == 200
    data = get_resp.json()
    assert data["id"] == project_id

    # Очистка: удаляем созданный проект (если API поддерживает DELETE)
    delete = {'deleted': True}
    requests.put(
        f"{base_URL}projects/{data['id']}", json=delete, headers=headers)


def test_get_project_negative_invalid_id():
    invalid_id = -1
    response = requests.get(
        f"{base_URL}projects/{invalid_id}", headers=headers)

    assert response.status_code == 404
