from abc import ABC, abstractmethod
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class ElementScraper(ABC):
    @abstractmethod
    def scrape_xpath(self, driver: WebDriver, value: str) -> WebElement:
        pass

    @abstractmethod
    def scrape_id(self, driver: WebDriver, value: str) -> WebElement:
        pass

    @abstractmethod
    def scrape_class(self, driver: WebDriver, value: str) -> WebElement:
        pass

    @abstractmethod
    def scrape_tag_name(self, driver: WebDriver, value: str) -> WebElement:
        pass