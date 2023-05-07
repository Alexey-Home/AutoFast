# -*- coding: utf8 -*-
from fake_useragent import UserAgent
import time
from sys import platform
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def set_options():
    """Настройка параметров options"""
    options = webdriver.ChromeOptions()

    ua = UserAgent(browsers=["chrome", "edge", "internet explorer", "firefox", "safari", "opera"])

    # user-agent
    options.add_argument(f"user-agent={ua.random}")

    # accept
    options.add_argument("accept=text/html,application/xhtml+xml,application/xml;q=0.9,image/"
                         "avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9")

    # for ChromeDriver version 79.0.3945.16 or over
    options.add_argument("--disable-blink-features=AutomationControlled")

    # headless mode
    options.add_argument("--no-sandbox")
    options.headless = True
    return options


def path_setting():
    """Возвращает путь для cromedriver в зависимости от системы"""

    if platform == "win32":
        return r"C:\Users\domah\PycharmProjects\AutoFast\chromedriver.exe"
    else:
        return "/home/my_bot/chromedriver"


def saving_page(driver, url):
    """Сохранение страницы """

    print("Открываю страницу...")
    driver.get(url=url)

    time.sleep(5)

    try:
        print("Сохраняю страницу...")
        with open("pages_html/page.html", "w", encoding="utf-8") as file:
            file.write(driver.page_source)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

    print("Готово!")


def get_page(url):

    options = set_options()

    path = path_setting()

    s = Service(path)
    driver = webdriver.Chrome(service=s, options=options)

    saving_page(driver, url)


if __name__ == "__main__":
    url = "https://www.avito.ru/all/avtomobili?cd=1&p=1"
    get_page(url)
