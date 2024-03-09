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

