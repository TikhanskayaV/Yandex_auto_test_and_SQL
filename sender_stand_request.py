# Виктория Тиханская, 19-я когорта — Финальный проект. Инженер по тестированию плюс
import data
import requests
import configuration


# Создание заказа
def post_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=order_body, headers=data.headers)


response = post_new_order(data.order_body)
track = response.json()["track"]
print(response.status_code)
print(response.json())


# Проверка, что по треку заказа можно получить данные о заказе.
def get_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER + str(track),
                        headers=data.headers)


response = get_order(track)
print(response.status_code)
print(response.json())
