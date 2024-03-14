import allure
import requests
import pytest
from data import TestData
from data import url
from data import ErrorsMessages as EM


class TestCreateCourier:

    @allure.title('Проверка успешного создания курьера')
    @allure.description('Позитивный сценарий тестирования ручки "Создание курьера" POST /api/v1/courier.'
                        'Проверяет, что курьера можно создать, '
                        'чтобы создать курьера, нужно передать в ручку все обязательные поля, '
                        'успешный запрос возвращает {"ok":true}.')
    def test_success_create_courier(self, new_courier):
        response = new_courier[0]
        assert response.status_code == 201
        assert response.json() == {'ok': True}

    @allure.title('Проверка неуспешного создания дублирующего курьера')
    @allure.description('Негативный сценарий тестирования ручки "Создание курьера" POST /api/v1/courier.'
                        'Проверяет, что нельзя создать двух одинаковых курьеров.')
    def test_fail_create_same_courier(self, new_courier):
        login = new_courier[1][0]
        password = new_courier[1][1]
        first_name = new_courier[1][2]
        same_payload = {
            'login': login,
            'password': password,
            'firstName': first_name
        }
        response = requests.post(f'{url}/api/v1/courier', data=same_payload)
        assert response.status_code == 409
        assert response.json()['message'] == EM.create_courier_error_409

    @allure.title('Проверка неуспешного создания курьера с пустым обязательным полем')
    @allure.description('Негативный сценарий тестирования ручки "Создание курьера" POST /api/v1/courier.'
                        'Проверяет, что если одного из полей нет, запрос возвращает ошибку;')
    @pytest.mark.parametrize('payload', TestData.empty_field)
    def test_fail_create_courier_with_empty_field(self, payload):
        response = requests.post(f'{url}/api/v1/courier', data=payload)
        assert response.status_code == 400
        assert response.json()['message'] == EM.create_courier_error_400

    @allure.title('Проверка неуспешного создания курьера с существующим логином')
    @allure.description('Негативный сценарий тестирования ручки "Создание курьера" POST /api/v1/courier.'
                        'Проверяет, что если создать пользователя с логином, который уже есть, возвращается ошибка.')
    def test_fail_create_courier_with_same_login(self, new_courier):
        login = new_courier[1][0]
        password = new_courier[1][1] + 'meow'
        first_name = new_courier[1][2] + 'meow'
        same_login_payload = {
            'login': login,
            'password': password,
            'firstName': first_name
        }
        response = requests.post(f'{url}/api/v1/courier', data=same_login_payload)
        assert response.status_code == 409
        assert response.json()['message'] == EM.create_courier_error_409
