import allure
import requests
from data import url

class TestOrderList:

    @allure.title('Проверка успешного получения списка заказов')
    @allure.description('Позитивный сценарий тестирования ручки "Получение списка заказов" GET /api/v1/orders.'
                        'Проверяет, что в тело ответа возвращается список заказов.')
    def test_get_order_list(self):
        response = requests.get(f'{url}/api/v1/orders')
        assert response.status_code == 200
        response_body = response.json()['orders']
        assert isinstance(response_body, list)