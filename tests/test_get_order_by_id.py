import allure
import pytest
import requests
from data import OrderData
from data import url

class TestGetOrderById:

    @allure.title('Проверка успешного получения заказа по его id')
    @allure.description('Позитивный сценарий тестирования ручки "Получить заказ по его номеру" GET /api/v1/orders/track.'
                        'Успешный запрос возвращает объект с заказом.')
    @pytest.mark.parametrize('colors', OrderData.colors)
    def test_get_order_by_id(self, colors):
        OrderData.order_data['colors'] = [colors]
        payload = OrderData.order_data
        response = requests.post(f'{url}/api/v1/orders', data=payload)
        track_id = response.json().get('track')
        payload_track = {'t': f'{track_id}'}
        response_order = requests.get(f'{url}/api/v1/orders/track', params=payload_track)
        assert response_order.status_code == 200
        response_order_body = response_order.json()['order']
        assert isinstance(response_order_body, dict)

    @allure.title('Проверка неуспешного получения заказа без указания его id')
    @allure.description('Негативный сценарий тестирования ручки "Получить заказ по его номеру" GET /api/v1/orders/track.'
                        'Запрос без номера заказа возвращает соответсвующую ошибку.')
    def test_get_order_without_id(self):
        response = requests.get(f'{url}/api/v1/orders/track')
        assert response.status_code == 400
        assert response.json()['message'] == 'Недостаточно данных для поиска'

    @allure.title('Проверка неуспешного получения заказа при указании несущетвующего id')
    @allure.description('Негативный сценарий тестирования ручки "Получить заказ по его номеру" GET /api/v1/orders/track.'
                        'Запрос с несуществующим заказом возвращает соответсвующую ошибку.')
    def test_get_order_no_exist_id(self):
        payload_track = {'t': 0}
        response = requests.get(f'{url}/api/v1/orders/track', params=payload_track)
        assert response.status_code == 404
        assert response.json()['message'] == 'Заказ не найден'