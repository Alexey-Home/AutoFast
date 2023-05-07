# -*- coding: utf8 -*-
from scanning import get_page
from bs4 import BeautifulSoup


def car_card_search() -> list:
    """Возвращает список карточек с машинми"""

    with open("pages_html/page.html", "r", encoding="utf-8") as file:
        page_html = file.read()

    soup = BeautifulSoup(page_html, "lxml")

    cards = soup.find("div", class_="items-items-kAJAg")\
        .find_all("div", class_="iva-item-root-_lk9K photo-slider-slider-S15A_ iva-item-list-rfgcH "
                                "iva-item-redesign-rop6Piva-item-responsive-_lbhG"
                                " items-item-My3ih items-listItem-Gd1jN js-catalog-item-enum")
    return cards


def get_urls(cards: list) -> list:
    """Возвращает список urls на автомобили"""
    return ["https://www.avito.ru" + card.find("a", class_="iva-item-sliderLink-uLz1v").get("href") for card in cards]


def main():
    get_page("https://www.avito.ru/all/avtomobili?cd=1&p=1")

    cards = car_card_search()

    urls = get_urls(cards)
    print(*urls)


if __name__ == '__main__':
    main()
