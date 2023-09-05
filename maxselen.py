from selenium import webdriver
from selenium.webdriver.firefox.service import Service as GeckoDriverManager

from webdriver_manager.microsoft import IEDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import time

# from faker import Faker
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.edge import EdgeDriverManager


from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import random

from selenium.webdriver.support import expected_conditions as EC



class Maxselen:
    def __init__(self, browser="Chrome"):
        print(f"Initialization for {browser}")
        if browser == "Chrome":
            opts = webdriver.ChromeOptions()
            self.WebDriver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=opts)
        elif browser == "Firefox":
            opts = webdriver.FirefoxOptions()
            self.WebDriver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=opts)
        elif browser == "Edge":
            opts = webdriver.EdgeOptions()
            self.WebDriver = webdriver.Edge(service=EdgeDriverManager().install(), options=opts)

        else:
            raise ValueError(f"Unsupported browser: {browser}")

        self.WebDriver.maximize_window()


if __name__ == "__main__":
    first = Maxselen("Chrome")
    first.WebDriver.get("https://google.com")
    time.sleep(10)

    print("test 2", __name__)
