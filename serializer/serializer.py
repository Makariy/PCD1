import csv
from models.graphics import GraphicsCardsWithBrand


class Serializer:
    def __init__(
            self,
            base_path: str = "./"
    ):
        self._base_path = base_path

    def serialize(self, graphics_cards_with_brand: GraphicsCardsWithBrand):
        """
        Hace la exportacion de las tarjetas graficas a una archivo.
        El nombre del archivo tiene que ser f"{graphics_cards_with_brand.brand}.csv"
        y localizado en el directorio self._base_path
        """


