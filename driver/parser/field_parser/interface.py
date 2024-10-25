from abc import ABC, abstractmethod


class IFieldParser(ABC):
    @staticmethod
    @abstractmethod
    def parse() -> str | int | float | None:
        pass

    def clean(self):
        pass
