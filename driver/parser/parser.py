from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from driver import Driver
from models.graphics import GraphicsCard

from re import search


class PageParser:
    def __init__(self, driver: Driver):
        self._driver = driver

    def __get_parent_brand(self, chipset: str) -> str:
        """
        Devuelve la marca del chipset
        """
        if search(r"^(?:NVS|Quadro|RTX|T\d{3,4}|TITAN|GeForce)\s", chipset):
            return "NVIDIA"
        elif search(r"^(?:Radeon|FirePro|FireGL|Vega)\s", chipset):
            return "AMD"
        elif search(r"^Arc\s", chipset):
            return "Intel"
        else:
            return "Unknown"

    def __get_star_rating(self, raw_card: WebElement) -> tuple[int, float]:
        """
        Devuelve la cantidad de estrellas y la cantidad de usuarios que han
        votado
        """
        # Get the stars list
        stars = raw_card.find_elements(By.XPATH, "./td[contains(@class, 'td__rating')]/ul/li")
        count = 0
        for star in stars:
            # Check if the svg star is full
            if star.find_element(By.TAG_NAME, "svg").get_attribute("class") == "shape-star-full":
                count += 1

        # Get the number of voters
        voters = raw_card.find_element(By.XPATH, "./td[contains(@class, 'td__rating')]").text
        # Extract the number of voters
        voters = int(voters.strip().replace("(", "").replace(")", ""))

        return count, voters

    def __convert_if_exists(self, element: str, fun: float | int) -> float | int | None:
        """
        Convierte el elemento a float o int si es posible
        """
        try:
            return fun(element.strip())
        except ValueError:
            return None

    def __clean_elements(self, memory: str, core_clock: str, boost_clock: str, length: str, price: str) -> tuple:
        """
        Limpia los campos de memoria, core_clock, boost_clock y price
        """
        memory = float(memory.replace("GB", "")) * 1024
        core_clock = self.__convert_if_exists(core_clock.replace("MHz", ""), int)
        boost_clock = self.__convert_if_exists(boost_clock.replace("MHz", ""), int)
        length = self.__convert_if_exists(length.replace("mm", ""), int)
        price = self.__convert_if_exists(price.replace("$", "").replace("Add", ""), float)
        return memory, core_clock, boost_clock, length, price

    def _parse_raw_card(self, raw_card: WebElement) -> GraphicsCard:
        """
        Lo mismo que antes, selecciona todos los campos y los
        devuelve como instancia de GraphicsCard
        """
        name = raw_card.find_element(By.XPATH, "./td[contains(@class, 'td__name')]//div[@class='td__nameWrapper']/p").text
        chipset = raw_card.find_element(By.XPATH, "./td[contains(@class, 'td__spec--1')]").text
        memory = raw_card.find_element(By.XPATH, "./td[contains(@class, 'td__spec--2')]").text
        core_clock = raw_card.find_element(By.XPATH, "./td[contains(@class, 'td__spec--3')]").text
        boost_clock = raw_card.find_element(By.XPATH, "./td[contains(@class, 'td__spec--4')]").text
        length = raw_card.find_element(By.XPATH, "./td[contains(@class, 'td__spec--6')]").text
        price = raw_card.find_element(By.XPATH, "./td[contains(@class, 'td__price')]").text

        parent_brand = self.__get_parent_brand(chipset)

        memory, core_clock, boost_clock, length, price = self.__clean_elements(memory, core_clock, boost_clock, length, price)
        user_score, user_ratings_count = self.__get_star_rating(raw_card)

        return GraphicsCard(
            name=name,
            parent_brand=parent_brand,
            price=price,
            memory=memory,
            core_clock=core_clock,
            core_boost_clock=boost_clock,
            length=length,
            user_score=user_score,
            user_ratings_count=user_ratings_count,
            chipset=chipset
        )

    def parse(self) -> list[GraphicsCard]:
        """
        Busca todas las filas con tarjetas graficas y las pasa a self._parse_raw_card
        """
        tabla = self._driver.find_element(By.ID, "category_content")
        rows = tabla.find_elements(By.XPATH, "./tr")
        return [self._parse_raw_card(card) for card in rows]
