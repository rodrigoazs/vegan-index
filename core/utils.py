import re
import time

import pyautogui
import pyperclip
from bs4 import BeautifulSoup


def get_countries(text):
    matches = re.findall(r"([a-zA-Z\s\-]*)\([0-9]*\)", text.replace("\n", ""))
    return matches


def get_cities(text):
    matches = re.findall(r"([a-zA-Z\s\-]*)\(([0-9]*)\)", text.replace("\n", ""))
    return matches


def copy_text():
    pyautogui.move(0, 50)
    pyautogui.hotkey("command", "a")
    time.sleep(2)
    pyautogui.hotkey("command", "c")
    return pyperclip.paste()


def change_url(url):
    pyautogui.moveTo(253, 97, duration=1, tween=pyautogui.easeInOutQuad)
    pyautogui.click()
    pyautogui.write(url)
    pyautogui.press("enter")
    time.sleep(5)


def get_page_source():
    pyautogui.hotkey("option", "command", "u")
    time.sleep(2)
    pyautogui.hotkey("command", "a")
    time.sleep(1)
    pyautogui.hotkey("command", "c")
    html = pyperclip.paste()
    time.sleep(1)
    pyautogui.hotkey("command", "w")
    return html


def get_urls(html):
    soup = BeautifulSoup(html, "html.parser")
    results = soup.find(id="full-site-content")
    results = results.find(class_="region-panel-list")
    job_elements = results.find_all("div", class_="break-inside-avoid")
    data = []
    for job_element in job_elements:
        a = job_element.find_all("a", href=True)
        href = a[0]["href"]
        matches = re.search("^\/([a-z\-\_]*)\/([a-z\-\_]*)\/$", href)
        continent = matches.groups()[0]
        country = matches.groups()[1]
        nes = job_element.find_all("div")
        name = nes[1].next
        data.append([name, continent, country])
    return data
