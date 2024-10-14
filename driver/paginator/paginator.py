from driver import Driver


class Paginator:
    def __init__(self, driver: Driver):
        self._driver = driver

    def has_next_page(self) -> bool:
        """
        Se busca la flecha debajo de la pagina y si no la hay, se devuelve True si la hay
        """

    def navigate_to_next_page(self) -> None:
        """
        Se busca la flecha debajo y si se pulsa
        (o se coge su URL y se hace self._driver.get(<URL>))
        """
