from .interface import IFieldParser

from bs4 import Tag

from re import match


class NameParser(IFieldParser):
    def __init__(self):
        pass

    @staticmethod
    def parse(tr: Tag) -> str:
        name = tr.select_one("td.td__name div.td__nameWrapper p").find(text=True, recursive=False)
        return name


class ParentBrandParser(IFieldParser):
    def __init__(self):
        pass

    @staticmethod
    def parse(tr: Tag) -> str:
        chipset = ChipsetParser.parse(tr)

        if match(r"(?:NVS|Quadro|RTX|T\d{3,4}|TITAN|GeForce)\s", chipset):
            return "NVIDIA"
        elif match(r"(?:Radeon|FirePro|FireGL|Vega)\s", chipset):
            return "AMD"
        elif match(r"Arc\s", chipset):
            return "Intel"
        else:
            return "Unknown"


class PriceParser(IFieldParser):
    def __init__(self):
        pass

    @staticmethod
    def parse(tr: Tag) -> float:
        price = tr.select_one("td.td__price").find(text=True, recursive=False)
        if price:
            price = convert_if_exists(price.replace("$", ""), float)
        return price


class MemoryParser(IFieldParser):
    def __init__(self):
        pass

    @staticmethod
    def parse(tr: Tag) -> int:
        memory = tr.select_one("td.td__spec--2").find(text=True, recursive=False)
        if memory:
            memory = convert_if_exists(memory.replace("GB", ""), float)
        return memory * 1024 if memory else None


class CoreClockParser(IFieldParser):
    def __init__(self):
        pass

    @staticmethod
    def parse(tr: Tag) -> int:
        core_clock = tr.select_one("td.td__spec--3").find(text=True, recursive=False)
        if core_clock:
            core_clock = convert_if_exists(core_clock.replace("MHz", ""), int)
        return core_clock


class BoostClockParser(IFieldParser):
    def __init__(self):
        pass

    @staticmethod
    def parse(tr: Tag) -> int:
        boost_clock = tr.select_one("td.td__spec--4").find(text=True, recursive=False)
        if boost_clock:
            boost_clock = convert_if_exists(boost_clock.replace("MHz", ""), int)
        return boost_clock


class LengthParser(IFieldParser):
    def __init__(self):
        pass

    @staticmethod
    def parse(tr: Tag) -> int:
        length = tr.select_one("td.td__spec--6").find(text=True, recursive=False)
        if length:
            length = convert_if_exists(length.replace("mm", ""), int)
        return length


class UserScoreParser(IFieldParser):
    def __init__(self):
        pass

    @staticmethod
    def parse(tr: Tag) -> int:
        stars = tr.select_one("td.td__rating").get("data-ci")
        stars = int(stars) if stars else 0

        return stars // 200 + 1 if stars else 0


class UserRatingsCountParser(IFieldParser):
    def __init__(self):
        pass

    @staticmethod
    def parse(tr: Tag) -> int:
        voters = tr.select_one("td.td__rating").find(text=True, recursive=False)
        if voters:
            voters = convert_if_exists(voters.replace("(", "").replace(")", ""), int)
        return voters if voters else 0


class ChipsetParser(IFieldParser):
    def __init__(self):
        pass

    @staticmethod
    def parse(tr: Tag) -> str:
        chipset = tr.select_one("td.td__spec--1").find(text=True, recursive=False)
        return chipset


def convert_if_exists(element: str, fun: float | int) -> float | int | None:
    try:
        return fun(element.strip())
    except ValueError:
        return None
