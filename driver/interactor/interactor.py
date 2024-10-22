from driver import Driver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Interactor:
    def __init__(self, driver: Driver, base_url: str):
        self._driver = driver
        self._base_url = base_url

    def accept_cookies(self) -> None:
        """
        Busca el box correspondiente a aceptar cookies
        y lo pulsa
        """

        try:
            accept_cookies_button = self._driver.find_element(By.CSS_SELECTOR, 'a[aria-label="allow cookies"]')

            if accept_cookies_button.is_enabled() and accept_cookies_button.is_displayed():
                accept_cookies_button.click()

        except NoSuchElementException:
            print("No cookies to accept!")

        except ElementClickInterceptedException:
            print("Cookies couldnt be accepted!")

    def select_vendor(self, vendor_name: str) -> None:
        """
        Selecciona del filtro Manufacturer a la izquierda (#filterdiv_m)
        todos los li y busca uno que tenga dentro label como el vendor_name. Una
        vez lo tiene, pulsa el input y espera a que se cargue
        """

        try:
            WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located((By.ID, "filterdiv_m")))

            vendors = self._driver.find_elements(By.CSS_SELECTOR, "#filterdiv_m li")

            for vendor in vendors:
                label = vendor.find_element(By.TAG_NAME, "label")
                if vendor_name.lower() in label.text.lower():
                    checkbox = vendor.find_element(By.TAG_NAME, "input")
                    self._driver.execute_script("arguments[0].click();", checkbox)

                    WebDriverWait(self._driver, 10).until(EC.invisibility_of_element_located((By.CLASS_NAME,
                                                                                              "loading-spinner")))
                    print(f"Vendor '{vendor_name}' selected successfully.")
                    return

            print(f"Vendor '{vendor_name}' was not found in the list.")

        except NoSuchElementException:
            print("No vendors are displayed!")

        except ElementClickInterceptedException:
            print("Not able to click the vendor checkbox!")
