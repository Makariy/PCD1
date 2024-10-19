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
        for card in graphics_cards_with_brand:
            with open(f"{self._base_path}/{graphics_cards_with_brand.brand}.csv", "w") as file:
                writer = csv.writer(file)
                writer.writerow(["name", "parent_brand", "price", "memory", "memory_type", "user_score", "user_ratings_count"])
                for card in graphics_cards_with_brand.graphics_cards:
                    writer.writerow([card.name, card.parent_brand, card.price, card.memory, card.memory_type, card.user_score, card.user_ratings_count])
