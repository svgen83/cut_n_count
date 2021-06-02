import requests
from urllib.parse import urlparse
import os
from dotenv import load_dotenv
import argparse


def shorten_link(token, url):
    bitlink_endpoint = "https://api-ssl.bitly.com/v4/bitlinks"
    bitlink_header = {"Authorization": token}
    bitlink_body = {"long_url": url}
    response = requests.post(bitlink_endpoint,
                             json=bitlink_body,
                             headers=bitlink_header)
    response.raise_for_status()
    bitlink_resp = response.json()
    return bitlink_resp["link"]


def count_clicks(token, link_without_scheme):
    url_template = "https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary"
    clicks_endpoint = url_template.format(link_without_scheme)
    headers = {"Authorization": token}
    params = {"unit": "day", "units": -1}
    response = requests.get(clicks_endpoint, headers=headers, params=params)
    response.raise_for_status()
    clicks = response.json()
    return clicks["total_clicks"]


def delete_url_scheme(url):
    url_fragments = urlparse(url)
    return "".join(url_fragments[1:])


if __name__ == "__main__":
    load_dotenv()
    parser = argparse.ArgumentParser(description="""
    Сокращение длинных ссылок и
    подсчет перехода по коротким ссылкам
    """)
    parser.add_argument("url", help="input e-link")
    args = parser.parse_args()
    url = args.url
    link_without_scheme = delete_url_scheme(url)
    token = os.getenv("BITLY_TOKEN")
    error_msg = """
    Ошибка. Страница не найдена.
    Возможно, Вы указали не ту ссылку
    или ошиблись при вводе.
    Введите ссылку заново
    """
    bitlink_endpoint_template = "https://api-ssl.bitly.com/v4/bitlinks/{}"
    bitlink_endpoint = bitlink_endpoint_template.format(link_without_scheme)
    headers = {"Authorization": token}
    response = requests.get(bitlink_endpoint, headers=headers)
    try:
        if response.ok:
            print("Количество переходов по короткой ссылке: ",
                  count_clicks(token, link_without_scheme))
        else:
            print("Короткая ссылка: ", shorten_link(token, url))
    except requests.HTTPError:
        print(error_msg)
