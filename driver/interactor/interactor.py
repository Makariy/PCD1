from driver import Driver


class Interactor:
    def __init__(self, driver: Driver, base_url: str):
        self._driver = driver
        self._base_url = base_url

    def select_vendor(self, vendor_name: str):
        """
        Primero, se va al self._base_url.
        A la izquierda donde estan los filtros, pulsa "ver mas"
        y elige la marca por su nombre.
        Despues espera hasta que se cargue la pagina
        """
