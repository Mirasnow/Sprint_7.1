import datetime
from datetime import date


url = 'http://qa-scooter.praktikum-services.ru'

class TestData:
    empty_field = [
        {'login': 'test1', 'first_name': 'Mira'},
        {'password': 'hello123', 'first_name': 'Mira'},
    ]


class OrderData:
    colors = [['BLACK'], ['GREY'], ['BLACK', 'GREY'], []]

    deliveryDate = (date.today() + datetime.timedelta(days=1)).strftime("%d.%m.%Y")

    order_data = {
        'firstName': 'Акакий',
        'lastName': 'Башмачкин',
        'address': 'Калинкин мост',
        "metroStation": 4,
        'phone': "+79990003333",
        'rentTime': 3,
        'deliveryDate': deliveryDate,
        'comment': 'Привезите мою шинель'
    }

class ErrorsMessages:
    courier_login_error_400 = 'Недостаточно данных для входа'
    courier_login_error_404 = 'Учетная запись не найдена'
    create_courier_error_400 = 'Недостаточно данных для создания учетной записи'
    create_courier_error_409 = 'Этот логин уже используется. Попробуйте другой.'
    delete_courier_error_404 = 'Курьера с таким id нет.'
    track_order_error_400 = 'Недостаточно данных для поиска'
    track_order_error_404 = 'Заказ не найден'
    accept_order_error_400 = 'Недостаточно данных для поиска'
    accept_order_courier_id_error_404 = 'Курьера с таким id не существует'
    accept_order_order_id_error_404 = 'Заказа с таким id не существует'

