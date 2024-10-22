import csv
from models.graphics import GraphicsCardsWithBrand, GraphicsCard


class Serializer:
    def __init__(
            self,
            base_path: str = "./"
    ):
        self._base_path = base_path

    def _get_graphics_fields_names(self) -> list[str]:
        return list(GraphicsCard.__annotations__.keys())

    def serialize(self, graphics_cards_with_brand: GraphicsCardsWithBrand):
        fields_names = self._get_graphics_fields_names()
        with open(f"{self._base_path}/{graphics_cards_with_brand.brand}.csv", "w") as file:
            writer = csv.writer(file)
            writer.writerow(fields_names)
            for card in graphics_cards_with_brand.graphics_cards:
                row = [getattr(card, field_name) for field_name in fields_names]
                writer.writerow(row)
