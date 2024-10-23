from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

from config import DEFAULT_DRIVER_WAIT_TIMEOUT
from driver import Driver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC


class Paginator:
    def __init__(self, driver: Driver):
        self._driver = driver

    def _get_current_page_element(self) -> WebElement | None:
        try:
            return self._driver.find_element(By.CSS_SELECTOR, ".pagination--current")
        except NoSuchElementException:
            return None

    def _get_current_page_index(self) -> int:
        current_page_element = self._get_current_page_element()
        current_page_index = 1
        if current_page_element is not None:
            current_page_index = int(current_page_element.get_attribute("innerText"))
        return current_page_index

    def _get_next_page_element(self) -> WebElement | None:
        next_page_index = self._get_current_page_index() + 1
        try:
            return self._driver.find_element(By.CSS_SELECTOR, f'a[href="#page={next_page_index}"]')
        except NoSuchElementException:
            return None

    def _get_pagination_element(self) -> WebElement:
        return self._driver.find_element(
            By.ID, "module-pagination"
        )

    def _await_pagination(self, pagination_element: WebElement):
        WebDriverWait(
            self._driver,
            DEFAULT_DRIVER_WAIT_TIMEOUT
        ).until(EC.staleness_of(pagination_element))

    def has_next_page(self) -> bool:
        return self._get_next_page_element() is not None

    def navigate_to_next_page(self) -> None:
        next_page_element: WebElement = self._get_next_page_element()

        pagination_element = self._get_pagination_element()
        self._driver.execute_script("arguments[0].click()", next_page_element)
        self._await_pagination(pagination_element)

