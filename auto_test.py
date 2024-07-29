# Виктория Тиханская, 19-я когорта — Финальный проект. Инженер по тестированию плюс
import data
import sender_stand_request


# Автотест
def test_get_order_and_code_is_200():
    # Выполнить запрос на создание заказа
    response = sender_stand_request.post_new_order(data.order_body)

    # Сохранить номер трека заказа
    track = response.json()["track"]

    # Выполнить запрос на получения заказа по треку заказа
    response_order = sender_stand_request.get_order(track)

    # Проверить, что код ответа равен 200.
    assert response_order.status_code == 200

