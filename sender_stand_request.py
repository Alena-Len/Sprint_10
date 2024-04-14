import configuration
import requests
import data


def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)


def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)


"""response = get_users_table()
print(response.status_code)"""


def post_new_user(body):
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
        json=body,
        headers=data.headers,
    )


"""response = post_new_user(data.user_body)
print(response.status_code)
print(response.json())"""


def get_user_token():
    response = post_new_user(data.user_body)
    return response.json().get("authToken")


def post_new_client_kit(kit_body):
    # data.headers["Authorization"] += get_user_token()
    # print(data.headers["Authorization"])
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_KITS_PATH,
        json=kit_body,
        headers=data.headers,
    )


def get_kit_body(kit_body):
    current_body = data.kit_body.copy()
    current_body["name"] = kit_body
    return current_body


"""response = get_kit_body(data.kit_body)
print(response)"""
