from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup

from driver import Driver
from models.graphics import GraphicsCard
from .element_parser import ElementParser


class PageParser:
    def __init__(self, driver: Driver):
        self._driver = driver

    def parse(self) -> list[GraphicsCard]:
        """
        Busca todas las filas con tarjetas graficas y las pasa a self._parse_raw_card
        """
        tabla = self._driver.find_element(By.ID, "category_content").get_attribute("innerHTML")
        tabla = BeautifulSoup(tabla, "html.parser")
        rows = tabla.find_all("tr")
        return [ElementParser.parse(row) for row in rows]
