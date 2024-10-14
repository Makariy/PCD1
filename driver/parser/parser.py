from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from driver import Driver
from models.graphics import GraphicsCard


class PageParser:
    def __init__(self, driver: Driver):
        self._driver = driver

    def _parse_raw_card(self, raw_card: WebElement) -> GraphicsCard:
        """
        Parseo de una tarjeta concreta.
        (Se tiene que separar en unas funciones mas cada una de las cuales
        busca un elemento concreto de GraphicsCard).
        Por ejemplo para obtener la memoria que hay, aplicas a product-card__title
        el regex tipo (\\d+)GB.
        Una vez se tienen todos los elementos, se juntan en GraphicsCard y se devuelve
        """
        ...

    def parse(self) -> list[GraphicsCard]:
        """
        Parseo de cada tarjeta grafica que hay en la pagina
        y lo devuelve como una lista
        """

        # Algo tipo
        # cards = []
        # for raw_card in self._driver.find_elements(By.CLASS_NAME, "product-card"):
        #     card = self._parse_raw_card(raw_card)
        #     cards.append(card)
        # return cards
