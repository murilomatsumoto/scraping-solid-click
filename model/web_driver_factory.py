from abc import ABC, abstractmethod
from selenium import webdriver 
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class WebDriverFactory(ABC):
    @abstractmethod
    def create_driver(self, headless: bool = True) -> WebDriver:
        pass

class ChromeDriverFactory(WebDriverFactory):
    def create_driver(self, headless: bool = True) -> WebDriver:
        options = Options()
        options.headless = headless
        chromedriver_path = ChromeDriverManager().install()
        service = Service(chromedriver_path)
        return webdriver.Chrome(service=service, options=options)
