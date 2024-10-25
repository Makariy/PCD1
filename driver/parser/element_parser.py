from bs4 import Tag

from .field_parser.field_parser import *
from models.graphics import GraphicsCard

from re import search


class ElementParser:
    def __init__(self):
        pass

    @staticmethod
    def parse(tr: Tag) -> GraphicsCard:
        name = NameParser.parse(tr)
        parent_brand = ParentBrandParser.parse(tr)
        chipset = ChipsetParser.parse(tr)
        memory = MemoryParser.parse(tr)
        core_clock = CoreClockParser.parse(tr)
        boost_clock = BoostClockParser.parse(tr)
        length = LengthParser.parse(tr)
        price = PriceParser.parse(tr)
        user_score = UserScoreParser.parse(tr)
        user_ratings_count = UserRatingsCountParser.parse(tr)

        return GraphicsCard(
            name=name,
            parent_brand=parent_brand,
            price=price,
            memory=memory,
            core_clock=core_clock,
            core_boost_clock=boost_clock,
            length=length,
            user_score=user_score,
            user_ratings_count=user_ratings_count,
            chipset=chipset
        )
