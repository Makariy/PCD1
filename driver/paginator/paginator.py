from driver import Driver


class Paginator:
    def __init__(self, driver: Driver):
        self._driver = driver

    def _get_page(self) -> int:
        """
        Devuelve la pagina actual sacandola del query de la URL
        Si no hay page especificado en los parametros de la URL,
        devuelve 1
        """
        ...

    def has_next_page(self) -> bool:
        """
        Busca las posibles paginas que se muestran en .pagination
        y compara si hay page + 1 (sacando page de self._get_page)
        """
        ...

    def navigate_to_next_page(self) -> None:
        """
        Pone en url page + 1
        """
        ...
