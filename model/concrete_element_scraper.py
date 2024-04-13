from model.element_scraper import ElementScraper
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class ConcreteElementScraper(ElementScraper):
    def scrape_xpath(self, driver: WebDriver, value: str) -> WebElement:
        return driver.find_element(By.XPATH, value)

    def scrape_id(self, driver: WebDriver, value: str) -> WebElement:
        return driver.find_element(By.ID, value)

    def scrape_class(self, driver: WebDriver, value: str) -> WebElement:
        return driver.find_element(By.CLASS_NAME, value)

    def scrape_tag_name(self, driver: WebDriver, value: str) -> WebElement:
        return driver.find_element(By.TAG_NAME, value)

