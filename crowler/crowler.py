from models.graphics import GraphicsCard, GraphicsCardsWithBrand

from driver.interactor.interactor import Interactor
from driver.paginator import Paginator
from driver.parser import PageParser

from driver import (
    create_webdriver,
    create_webdriver_options,
    Driver
)

from config import HEADLESS


class Crowler:
    def __init__(self, base_url: str):
        self._base_url = base_url

    def _get_graphics_cards_for_brand(
            self,
            driver: Driver,
            brand: str
    ) -> list[GraphicsCard]:
        """
        Pasa por el vendedor y devuelve todas sus tarjetas graficas
        """
        cards: list[GraphicsCard] = []

        parser = PageParser(driver)
        paginator = Paginator(driver)
        interactor = Interactor(
            driver=driver,
            base_url=self._base_url
        )
        interactor.select_vendor(brand)

        while True:
            cards = cards + parser.parse()
            if not paginator.has_next_page():
                break
            paginator.navigate_to_next_page()

        return cards

    def parse_brands(self, brands: list[str]):
        """
        Pasa por cada marca y parsea todas sus tarjetas graficas
        """
        driver = create_webdriver(
            create_webdriver_options(is_headless=HEADLESS)
        )

        graphics_cards_with_brands: list[GraphicsCardsWithBrand] = []
        for vendor in brands:
            graphics_cards = self._get_graphics_cards_for_brand(driver, vendor)
            graphics_cards_with_brands.append(GraphicsCardsWithBrand(
                brand=vendor,
                graphics_cards=graphics_cards
            ))

        return graphics_cards_with_brands
