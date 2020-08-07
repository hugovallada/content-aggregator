from typing import List, Dict
from bs4 import BeautifulSoup
import requests


def create_soup(url: str) -> BeautifulSoup:
    res = requests.get(url)
    return BeautifulSoup(res.text, "html.parser")


def scrap_realpython() -> Dict[str, str]:
    contents = {}
    url = "https://realpython.com"
    soup = create_soup(url)
    href = soup.find_all("div", {"class": "border-0"})

    for index, item in enumerate(href):
        if index > 2:
            break
        contents[href[index].find("h2").get_text()] = url + href[index].find("a").get(
            "href"
        )

    return contents


def scrap_manjaro_stable_updates() -> Dict[str, str]:
    contents = {}
    url = "https://forum.manjaro.org/c/announcements/stable-updates"
    soup = create_soup(url)
    href = soup.find_all("a", {"class": "raw-topic-link"})

    for index, item in enumerate(href):
        if index > 3:
            break
        if index == 0:
            continue
        contents[href[index].getText()] = href[index].get("href")

    return contents
