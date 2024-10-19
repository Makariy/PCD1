from driver import Driver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Paginator:
    def __init__(self, driver: Driver):
        self._driver = driver

    def accept_cookies(self) -> None:
        try:
            wait = WebDriverWait(self._driver, 10)
            accept_cookies_button = wait.until(
                EC.element_to_be_clickable((By.ID, "cookiesAcceptAll"))
            )

            accept_cookies_button.click()
            print("Accept cookies button clicked!")

        except NoSuchElementException:
            print("Accept cookies button not found!")
        except ElementClickInterceptedException:
            print("Accept cookies button not clickable!")

    def has_next_page(self) -> bool:
        """
        Se busca la flecha debajo de la pagina y si no la hay, se devuelve True si la hay
        """

        try:
            next_page_button = self._driver.find_element(By.CSS_SELECTOR, "button.sc-fYaxgZ:nth-child(3)")

            if next_page_button.is_displayed() and next_page_button.is_enabled():
                return True
            return False

        except NoSuchElementException:
            return False

    def navigate_to_next_page(self) -> None:
        """
        Se busca la flecha debajo y si se pulsa
        (o se coge su URL y se hace self._driver.get(<URL>))
        """
        try:
            next_page_button = self._driver.find_element(By.CSS_SELECTOR, "button.sc-fYaxgZ:nth-child(3)")

            if next_page_button.is_displayed() and next_page_button.is_enabled():
                next_page_button.click()
                print("Next page button clicked!")

        except NoSuchElementException:
            print("Next page button not found!")

        except ElementClickInterceptedException:
            print("Next page button not clickable!")
