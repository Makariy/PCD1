from driver import Driver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class Paginator:
    def __init__(self, driver: Driver):
        self._driver = driver

    def _get_page(self) -> int:
        """
        Devuelve la pagina actual sacandola del query de la URL
        Si no hay page especificado en los parametros de la URL,
        devuelve 1
        """

        try:
            current_page = self._driver.find_element(By.CSS_SELECTOR, ".pagination--current")
            page_number = int(current_page.text)

        except NoSuchElementException:
            return 1

        return page_number

    def has_next_page(self) -> bool:
        """
        Busca las posibles paginas que se muestran en .pagination
        y compara si hay page + 1 (sacando page de self._get_page)
        """

        next_possible_page = self._get_page() + 1
        next_page_selector = f'a[href="#page={next_possible_page}"]'

        try:
            next_page = self._driver.find_element(By.CSS_SELECTOR, next_page_selector)
            return True if next_page else False

        except NoSuchElementException:
            return False

    def navigate_to_next_page(self) -> None:
        """
        Pone en url page + 1
        """

        if self.has_next_page():

            next_possible_page = self._get_page() + 1

            search_bar = self._driver.current_url

            if self._get_page() == 1:
                final_search_bar = search_bar + "#page=2"

            else:
                final_search_bar = search_bar[:-1] + f"{next_possible_page}"

            self._driver.get(final_search_bar)
