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

    def select_vendor(self, vendor_name: str):
        """
        Selecciona del filtro Manufacturer a la izquierda (#filterdiv_m)
        todos los li y busca uno que tenga dentro label como el vendor_name. Una
        vez lo tiene, pulsa el input y espera a que se cargue
        """
