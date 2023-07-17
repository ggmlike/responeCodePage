import time
import requests
from requests.exceptions import RequestException, HTTPError


def scan_url(url):
    try:
        response = requests.get(url, allow_redirects=True)
        status_code = response.status_code

        if response.history:
            with open("result.txt", "a") as file:
                for redirect in response.history:
                    file.write(f"{redirect.url} {redirect.status_code} -> {response.url}: Перенаправление - поиск "
                               f"сссылки не сайте\n")
        else:
            status_messages = {
                200: "OK",
                400: "Ошибка клиента - поиск ссылки на сайте",
                500: "Обратиться к сис.администратору, страницы отправить на переобход"
            }

            with open("result.txt", "a") as file:
                file.write(f"{url}: {status_messages.get(status_code, f'Код ответа {status_code}')}\n")

    except (HTTPError, RequestException) as e:
        with open("result.txt", "a") as file:
            file.write(f"{url} недоступен: {str(e)}\n")


def main():
    with open("dataUrls.txt", "r") as file:
        urls = [url.strip() for url in file]

    for url in urls:
        scan_url(url)
        time.sleep(1)


print("Данные внесены в файл result.txt")

if __name__ == "__main__":
    main()