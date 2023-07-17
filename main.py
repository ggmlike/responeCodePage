import time
import requests
from requests.exceptions import RequestException, HTTPError
from tqdm import tqdm


def scan_url(url):
    try:
        response = requests.get(url, allow_redirects=True)
        status_code = response.status_code

        if response.history:
            with open("results.txt", "a") as file:
                for redirect in response.history:
                    file.write(
                        f"{redirect.url} {redirect.status_code} -> {response.url}: Перенаправление - поиск сссылки на "
                        f"сайте\n")

        else:
            status_messages = {
                200: "OK",
                400: "Код ответа 4** ошибка клиента",
                500: "Код ответ 5** - обратиться к сис.администратору, страницы отправить на переобход"
            }

            with open("results.txt", "a") as file:
                file.write(f"{url}: {status_messages.get(status_code, f'Код ответа {status_code}')}\n")

    except (HTTPError, RequestException) as e:
        with open("results.txt", "a") as file:
            file.write(f"{url} недоступен: {str(e)}\n")


def main():
    with open("dataUrls.txt", "r") as file:
        urls = [url.strip() for url in file]

    total_urls = len(urls)
    with tqdm(total=total_urls, desc="Прогресс") as pbar:
        for url in urls:
            scan_url(url)
            time.sleep(1)
            pbar.update(1)


if __name__ == "__main__":
    main()
    print(f"Проверка завершена, все записи занесены в файл")
