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



        tabla = self._driver.find_element(By.ID, "category_content")
        rows = tabla.find_elements(By.XPATH, "./tr/td[@class='td__name']/a")
        return [self._parse_raw_card(card)  for card in rows]
