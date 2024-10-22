from selenium.webdriver.remote.webelement import WebElement

from config import DEFAULT_DRIVER_WAIT_TIMEOUT
from driver import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Interactor:
    def __init__(self, driver: Driver, base_url: str):
        self._driver = driver
        self._base_url = base_url

    def _wait_for_element_by_id(self, element_id: str):
        WebDriverWait(
            self._driver,
            DEFAULT_DRIVER_WAIT_TIMEOUT
        ).until(EC.visibility_of_element_located((By.ID, element_id)))

    def _get_vendors(self) -> list[WebElement]:
        return self._driver.find_elements(By.CSS_SELECTOR, "#filterdiv_m li[class]")

    def _get_vendor_by_name(self, vendor_name: str) -> WebElement | None:
        for vendor in self._get_vendors():
            label = vendor.find_element(By.TAG_NAME, "label")
            if label.get_attribute("innerText").lower() == vendor_name.lower():
                return vendor

    def _select_vendor(self, vendor: WebElement):
        checkbox = vendor.find_element(By.TAG_NAME, "input")
        self._driver.execute_script("arguments[0].click();", checkbox)

    def select_vendor(self, vendor_name: str) -> None:
        self._driver.get(self._base_url)

        self._wait_for_element_by_id("filterdiv_m")
        vendor = self._get_vendor_by_name(vendor_name)
        self._select_vendor(vendor)

        self._wait_for_element_by_id("module-pagination")
