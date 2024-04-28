import configuration
import requests
import data


def create_order(order_body):
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
        json=order_body,
    )


def get_order_info(track_number):
    track_path = configuration.CREATE_ORDER_PATH + "/track?t=" + str(track_number)
    return requests.get(
        configuration.URL_SERVICE + track_path,
    )
