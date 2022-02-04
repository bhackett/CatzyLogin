import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By

import urllib3
from bs4 import BeautifulSoup
from colorama import Fore

url = "https://accounts.cartzy.com"

colr = {
    "black": Fore.LIGHTBLACK_EX, "magenta": Fore.LIGHTMAGENTA_EX,
    "blue": Fore.LIGHTBLUE_EX, "red": Fore.LIGHTRED_EX,
    "cyan": Fore.LIGHTCYAN_EX, "white": Fore.LIGHTWHITE_EX,
    "green": Fore.LIGHTGREEN_EX, "yellow": Fore.LIGHTYELLOW_EX
}


def cstring(color: str, s: str) -> str:
    """Add color to a string"""
    return color + s


def printc(color: str, s: str):
    """Print color string"""
    print(cstring(color, s))


def download_content_source(url):
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    return response.data.decode('utf-8')


while True:
    try:
        source = download_content_source(url)
        soup = BeautifulSoup(source, "html.parser")
        fnd = soup.find(class_="alert alert-info")
        resp = fnd.text
        fnd = resp.startswith("Store", 0)
        match fnd:
            case False:
                printc(colr['red'], f"Store Creation Not Available at {datetime.now()}")
            case True:
                printc(colr['green'], f"Store Can Now Be Created at {datetime.now()}")
    except:
        printc(colr['cyan'], "Can't find Catzy class on website")

    time.sleep(30)


def login():
    """
    browser = webdriver.Chrome()  # Retrieve chrome
    browser.get("https://accounts.cartzy.com")
    browser.maximize_window()
    username = browser.find_element(By.CLASS_NAME, "alert alert-info")

    username.click()  # Put cursor in userName element
    username.send_keys(user)  # Enter username
    password = browser.find_element(By.ID, 'password')
    password.click()  # Put cursor in password element
    password.send_keys(pw)  # Enter password
    browser.find_element(By.ID, 'privateComputerLabel').click()
    browser.find_element(By.ID, 'login').click()
    browser.find_element(By.CLASS_NAME, 'icon-zoom-out zoom-out').click()
    """