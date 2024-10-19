from driver import Driver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class Interactor:
    def __init__(self, driver: Driver, base_url: str):
        self._driver = driver
        self._base_url = base_url

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

    def select_vendor_in_display(self, vendor_name) -> None:

        try:
            vendor_elements = self._driver.find_elements(By.CSS_SELECTOR, "span.sc-rqYmI")
            for vendor_element in vendor_elements:
                if vendor_element.text == vendor_name:
                    vendor_element.click()
                    print(f"Clicked of {vendor_element.text}")
                    break


        except NoSuchElementException:
            print("Vendors name not found in display!")

        except ElementClickInterceptedException:
            print("Vendors name in display not clickable!")

    def select_vendor(self, vendor_name: str):
        """
        Primero, se va al self._base_url.
        A la izquierda donde estan los filtros, pulsa "ver mas"
        y elige la marca por su nombre.
        Despues espera hasta que se cargue la pagina
        """
        self._driver.get(self._base_url)
        self.accept_cookies()

        try:
            filter_vendor_button = self._driver.find_element(By.CSS_SELECTOR, "#searcher")

            if filter_vendor_button.is_displayed() and filter_vendor_button.is_enabled():
                filter_vendor_button.click()
                filter_vendor_button.send_keys(vendor_name + Keys.ENTER)
                self.select_vendor_in_display(vendor_name)


        except NoSuchElementException:
            print("No filter button was found!")

        except ElementClickInterceptedException:
            print("Filter button not clickable!")
