from selenium import webdriver
from selenium.webdriver.firefox.service import Service as GeckoDriverManager

from webdriver_manager.microsoft import IEDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import time

from faker import Faker
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as OperaService

from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import random

from selenium.webdriver.support import expected_conditions as EC

NAME = "name"
ID = "id"
TAG = "tag name"
XPATH = "xpath"
CLASS = "class name"
LINK = "link text"
PART_LINK = "partial link text"
CSS = "css selector"
fake = Faker()


class Maxselen:
    def __init__(self, browser="Chrome"):
        print(f"Initialization for {browser}")
        if browser == "Chrome":
            opts = webdriver.ChromeOptions()
            self.Web = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=opts)
        elif browser == "Firefox":
            opts = webdriver.FirefoxOptions()
            self.Web = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=opts)
        elif browser == "Edge":
            opts = webdriver.EdgeOptions()
            self.Web = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=opts)


        else:
            raise ValueError(f"Unsupported browser: {browser}")

        self.Web.maximize_window()

    def type_to_xpath(self, x_path, text):
        self.Web.find_element(XPATH, x_path).send_keys(text)

    def select_id(self, elem_id, value):
        Select(self.Web.find_element(ID, elem_id)).select_by_value(value)

    def select_name(self, elem_id, value):
        Select(self.Web.find_element(NAME, elem_id)).select_by_value(value)


if __name__ == "__main__":
    first = Maxselen("Firefox")
    first.Web.get("https://google.com")
    time.sleep(10)
