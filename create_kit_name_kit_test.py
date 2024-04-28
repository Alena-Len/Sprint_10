# Лень Алёна, 15-я когорта — Финальный проект. Инженер по тестированию плюс
import data
import sender_stand_request


def positive_assert():
    # создаем заказ и сохраняем полученный ответ
    create_order_response = sender_stand_request.create_order(data.order_body)
    # сохраняем в переменную полученный при создании заказа номер заказа
    track_number = create_order_response.json()["track"]
    # получаем инфо о заказе по имеющемуся номеру
    check_order_response = sender_stand_request.get_order_info(track_number)
    # проверяем, что код ответа при получении заказа по его трек номеру равен 200
    assert check_order_response.status_code == 200


# 1
def test_check_order_success_response():
    positive_assert()
