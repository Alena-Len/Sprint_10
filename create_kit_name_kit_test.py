import sender_stand_request


def positive_assert(kit_name):
    # В переменную kit_body сохраняется обновлённое тело запроса
    kit_body = sender_stand_request.get_kit_body(kit_name)
    # В переменную user_response сохраняется результат запроса на создание пользователя:
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    # Проверяется, что код ответа равен 201
    assert kit_response.status_code == 201
    # Проверяется, что имя набора в ответе соответсвует вводимому имени
    assert kit_response.json()["name"] == kit_name


def negative_assert(kit_name):
    # В переменную kit_body сохраняется обновлённое тело запроса
    kit_body = sender_stand_request.get_kit_body(kit_name)
    # В переменную user_response сохраняется результат запроса на создание пользователя:
    kit_response = sender_stand_request.post_new_client_kit(kit_body)

    # Проверяется, что код ответа равен 400
    assert kit_response.status_code == 400
    # Проверяется, что имя набора в ответе соответствует вводимому имени
    assert kit_response.json()["name"] == kit_name


# 1
def test_create_kit_1_symbol_in_name_get_success_response():
    positive_assert({"name": "a"})


# 2
def test_create_kit_511_symbol_in_name_get_success_response():
    positive_assert(
        {
            "name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"
        }
    )


# 3
def test_create_kit_0_symbol_get_failed_response():
    negative_assert({"name": ""})


# 4
def test_create_kit_512_symbol_get_failed_response():
    negative_assert(
        {
            "name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"
        }
    )


# 5
def test_create_kit_eng_symbol_in_name_get_success_response():
    positive_assert({"name": "QWErty"})


# 6
def test_create_kit_rus_symbol_in_name_get_success_response():
    positive_assert({"name": "Мария"})


# 7
def test_create_kit_has_special_symbol_in_first_name_get_success_response():
    positive_assert('"№%@",')


# 8
def test_create_kit_has_space_in_first_name_get_success_response():
    positive_assert("Человек и КО")


# 9
def test_create_kit_has_number_in_first_name_get_success_response():
    positive_assert("123")


# 10
def test_create_kit_without_param_get_failed_response():
    negative_assert({})


# 11
def test_create_kit_int_param_get_failed_response():
    negative_assert(123)
