import requests
import random
import string
import pytest
from data import url


@pytest.fixture
def new_courier():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login_pass = []

    # генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    # собираем тело запроса
    payload = {
        'login': login,
        'password': password,
        'firstName': first_name
    }

    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.post(f'{url}/api/v1/courier', data=payload)

    # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    # возвращаем список
    yield response, login_pass

    # удаляем созданную учетную запись курьера
    if response.status_code == 201:
        delete_payload = {
            'login': login_pass[0],
            'password': login_pass[1]
        }
        login_response = requests.post(f'{url}/api/v1/courier/login', data=delete_payload)
        courier_id = login_response.json().get('id')
        requests.delete(f'{url}/api/v1/courier{courier_id}')

