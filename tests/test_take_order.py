import allure
import requests
from data import url

class TestTakeOrder:

    @allure.title('Проверка, что можно успешно принять заказ')
    @allure.description('Позитивный сценарий тестирования ручки "Принять заказ" PUT /api/v1/orders/accept/:id.'
                        'Проверяет, что успешный запрос возвращает {"ok":true}.')
    def test_take_order(self, new_courier):
        response, login_pass = new_courier
        payload = {
            'login': login_pass[0],
            'password': login_pass[1]
        }
        response = requests.post(f'{url}/api/v1/courier/login', data=payload)
        courier_id = response.json().get('id')
        payload_courier_id = {'courierId': f'{courier_id}'}
        response_order = requests.get(f'{url}/api/v1/orders')
        order_id = response_order.json()['orders'][0]['id']
        response_take_order = requests.put(f'{url}/api/v1/orders/accept/{order_id}', params=payload_courier_id)
        assert response_take_order.status_code == 200
        assert response_take_order.json() == {'ok': True}

    @allure.title('Проверка, что заказ нельзя принять, если не передан id курьера')
    @allure.description('Негативный сценарий тестирования ручки "Принять заказ" PUT /api/v1/orders/accept/:id.'
                        'Проверяет, что если не передать id курьера, запрос вернёт соответсвующую ошибку.')
    def test_take_order_no_courierid(self):
        response_order = requests.get(f'{url}/api/v1/orders')
        order_id = response_order.json()['orders'][0]['id']
        response_take_order = requests.put(f'{url}/api/v1/orders/accept/{order_id}')
        assert response_take_order.status_code == 400
        assert response_take_order.json()['message'] == 'Недостаточно данных для поиска'

    @allure.title('Проверка, что заказ нельзя принять, если передан неверный id курьера')
    @allure.description('Негативный сценарий тестирования ручки "Принять заказ" PUT /api/v1/orders/accept/:id.'
                        'Проверяет, что если передать неверный id курьера, запрос вернёт соответсвующую ошибку.')
    def test_take_order_invalid_courierid(self):
        payload_courier_id = {'courierId': 0}
        response_order = requests.get(f'{url}/api/v1/orders')
        order_id = response_order.json()['orders'][0]['id']
        response_take_order = requests.put(f'{url}/api/v1/orders/accept/{order_id}', params=payload_courier_id)
        assert response_take_order.status_code == 404
        assert response_take_order.json()['message'] == 'Курьера с таким id не существует'

    @allure.title('Проверка, что заказ нельзя принять, если не передан id заказа')
    @allure.description('Негативный сценарий тестирования ручки "Принять заказ" PUT /api/v1/orders/accept/:id.'
                        'Проверяет, что если не передать id заказа, запрос вернёт соответсвующую ошибку.')
    def test_take_order_no_orderid(self):
        response_take_order = requests.put(f'{url}/api/v1/orders/accept/:id')
        assert response_take_order.status_code == 400
        assert response_take_order.json()['message'] == 'Недостаточно данных для поиска'

    @allure.title('Проверка, что заказ нельзя принять, если передан неверный id заказа')
    @allure.description('Негативный сценарий тестирования ручки "Принять заказ" PUT /api/v1/orders/accept/:id.'
                        'Проверяет, что если передать неверный id заказа, запрос вернёт соответсвующую ошибку.')
    def test_take_order_invalid_orderid(self, new_courier):
        response, login_pass = new_courier
        payload = {
            'login': login_pass[0],
            'password': login_pass[1]
        }
        response = requests.post(f'{url}/api/v1/courier/login', data=payload)
        courier_id = response.json().get('id')
        payload_courier_id = {'courierId': f'{courier_id}'}
        order_id = 0
        response_take_order = requests.put(f'{url}/api/v1/orders/accept/{order_id}', params=payload_courier_id)
        assert response_take_order.status_code == 404
        assert response_take_order.json()['message'] == 'Заказа с таким id не существует'