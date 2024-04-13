from model.element_scraper import ElementScraper
from model.web_driver_factory import ChromeDriverFactory
from time import sleep


class WebScraper:
    def __init__(self, driver_factory: ChromeDriverFactory, scrapy: ElementScraper):
        self.driver_factory = driver_factory
        self.scrapy = scrapy

    def scrape(self, text_to_send):
        # URL hardcoded ou qualquer outra forma de obter a URL
        url = 'https://google.com.br/'
        driver = self.driver_factory.create_driver(headless=False)
        try:
            driver.get(url)
            # Exemplo de uso do método scrape_id
            element = self.scrapy.scrape_id(driver, 'APjFqb')
            element.send_keys(text_to_send)
            element.submit()
            name = self.scrapy.scrape_xpath(driver, '//div[@class="PZPZlf ssJ7i xgAzOe"]')
            name_text = name.text
            print(name_text)
            price = self.scrapy.scrape_xpath(driver, '//span[@class="IsqQVc NprOob wT3VGc"]')
            price_text = price.text
            print(price_text)

            sleep(5)
        finally:
            driver.quit()
