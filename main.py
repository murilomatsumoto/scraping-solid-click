import click
from controller.web_scraper import WebScraper
from model.concrete_element_scraper import ConcreteElementScraper
from model.web_driver_factory import ChromeDriverFactory
from time import sleep

@click.command()
@click.argument('text_to_send')
def main(text_to_send):
    scraper = WebScraper(ChromeDriverFactory(), ConcreteElementScraper())
    scraper.scrape(text_to_send)

if __name__ == '__main__':
    main()