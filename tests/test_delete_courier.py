import allure
import requests
from data import url


class TestDeleteCourier:

    @allure.title('Проверка успешного удаления курьера')
    @allure.description('Позитивный сценарий тестирования ручки "Удаление курьера" DELETE /api/v1/courier/:id.'
                        'Проверяет, что курьера можно удалить,'
                        'успешный запрос возвращает{"ok":true};')
    def test_success_delete_courier(self, new_courier):
        response, login_pass = new_courier
        payload = {
            'login': login_pass[0],
            'password': login_pass[1]
        }
        response = requests.post(f'{url}/api/v1/courier/login', data=payload)
        courier_id = response.json().get('id')
        response_delete = requests.delete(f'{url}/api/v1/courier/{courier_id}')
        assert response_delete.status_code == 200
        assert response_delete.json() == {'ok': True}

    @allure.title('Проверка неуспешного удаления курьера')
    @allure.description('Негативный сценарий тестирования ручки "Удаление курьера" DELETE /api/v1/courier/:id.'
                        'Проверяет, что если отправить запрос с несуществующим id, вернётся ошибка.'
                        'Неуспешный запрос возвращает соответствующую ошибку')
    def test_delete_courier_no_exist_id(self):
        response_delete = requests.delete(f'{url}/api/v1/courier/0')
        assert response_delete.status_code == 404
        assert response_delete.json()['message'] == 'Курьера с таким id нет.'




