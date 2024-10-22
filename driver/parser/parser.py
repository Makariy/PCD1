from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from driver import Driver
from models.graphics import GraphicsCard


class PageParser:
    def __init__(self, driver: Driver):
        self._driver = driver

    def _parse_raw_card(self, raw_card: WebElement) -> GraphicsCard:
        """
        Lo mismo que antes, selecciona todos los campos y los
        devuelve como instancia de GraphicsCard
        """
        ...

    def parse(self) -> list[GraphicsCard]:
        """
        Busca todas las filas con tarjetas graficas y las pasa a self._parse_raw_card
        """

        # Algo tipo
        # cards = []
        # for raw_card in self._driver.find_elements(By.CLASS_NAME, "tr__product"):
        #     card = self._parse_raw_card(raw_card)
        #     cards.append(card)
        # return cards
