from dataclasses import dataclass


@dataclass
class GraphicsCard:
    name: str  # Ex. RTX 4060
    parent_brand: str  # Ex. NVIDIA, AMD, Intel

    price: float  # In Euro

    memory: float  # In MB

    core_clock: float  # In MHz
    core_boost_clock: float | None  # In MHz

    length: int  # In mm

    user_score: float  # From 0 to 5
    user_ratings_count: int  # Ex. 241

    chipset: str  # Ex. Radeon RX7900 XTX
    # Si se considera que necesitara mas datos, anadimos mas atributos


@dataclass
class GraphicsCardsWithBrand:
    brand: str  # Ex. MSI, ASUS
    graphics_cards: list[GraphicsCard]

    def __str__(self):
        return self.brand
