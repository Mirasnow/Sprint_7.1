import allure
import requests
import pytest
from data import url
from data import ErrorsMessages as EM


class TestCourierLogin:

    @allure.title('Проверка успешной авторизации курьера')
    @allure.description('Позитивный сценарий тестирования ручки "Логин курьера в системе" POST /api/v1/courier/login.'
                        'Проверяет успешную авторизацию курьера')
    def test_success_login(self, new_courier):
        response, login_pass = new_courier
        payload = {
            'login': login_pass[0],
            'password': login_pass[1]
        }
        response = requests.post(f'{url}/api/v1/courier/login', data=payload)
        assert response.status_code == 200
        assert 'id' in response.json()

    @allure.title('Проверка неуспешной авторизации, если неправильно указать логин или пароль')
    @allure.description('Негативный сценарий тестирования ручки "Логин курьера в системе" POST /api/v1/courier/login.'
                        'Проверяет, что система вернёт ошибку, если неправильно указать логин или пароль')
    @pytest.mark.parametrize('invalid_data', ['login', 'password'])
    def test_invalid_login_or_password(self, new_courier, invalid_data):
        login_pass = new_courier[1]
        payload = {
            'login': login_pass[0],
            'password': login_pass[1]
        }
        payload[invalid_data] += 'meow'
        response = requests.post(f'{url}/api/v1/courier/login', data=payload)
        assert response.status_code == 404
        assert response.json()['message'] == EM.courier_login_error_404

    # у теста логина без пароля статус код 504 - это баг апи, обсуждали с наставником в пачке
    # сказали оставить так и написать коммент о баге апи
    @allure.title('Проверка неуспешной авторизации, если не указать логин или пароль')
    @allure.description('Негативный сценарий тестирования ручки "Логин курьера в системе" POST /api/v1/courier/login.'
                        'Проверяет, что система вернёт ошибку, '
                        'если попытаться авторизоваться не заполнив обязательное поле логин или пароль')
    @pytest.mark.parametrize('no_data', ['login', 'password'])
    def test_no_login_or_password(self, new_courier, no_data):
        login_pass = new_courier[1]
        payload = {
            'login': login_pass[0],
            'password': login_pass[1]
        }
        payload = {key: value for key, value in payload.items() if key != no_data}
        response = requests.post(f'{url}/api/v1/courier/login', data=payload)
        assert response.status_code == 400
        assert response.json()['message'] == EM.courier_login_error_400
