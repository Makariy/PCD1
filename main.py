from config import (
    BRANDS_TO_PARSE,
    PCCOMPONENTS_GRAPHICS_URL
)
from crowler.crowler import Crowler
from models.graphics import GraphicsCardsWithBrand
from serializer.serializer import Serializer


def serialize_graphics_cards_with_brands(
        graphics_cards_with_brands: list[GraphicsCardsWithBrand]
):
    serializer = Serializer()

    for graphics_card_with_brand in graphics_cards_with_brands:
        serializer.serialize(graphics_card_with_brand)


def main():
    crowler = Crowler(PCCOMPONENTS_GRAPHICS_URL)
    graphics_cards_with_brands = crowler.parse_brands(BRANDS_TO_PARSE)
    serialize_graphics_cards_with_brands(graphics_cards_with_brands)


if __name__ == "__main__":
    main()
