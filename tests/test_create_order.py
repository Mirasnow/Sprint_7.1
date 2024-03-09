import allure
import pytest
import requests
from data import OrderData
from data import url

class TestCreateOrder:

    @allure.title('Проверка успешного создания заказа')
    @allure.description('Позитивный сценарий тестирования ручки "Создание заказа" POST /api/v1/orders.'
                        'Проверяет, что заказ можно создать,'
                        'при создании заказа можно использовать различные комбинации цветов'
                        'тело ответа содержит track.')
    @pytest.mark.parametrize('colors', OrderData.colors)
    def test_create_order(self, colors):
        OrderData.order_data['colors'] = [colors]
        payload = OrderData.order_data
        response = requests.post(f'{url}/api/v1/orders', data=payload)
        assert response.status_code == 201
        assert 'track' in response.json()