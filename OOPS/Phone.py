import logging
from dataclasses import dataclass
from OOPS.Item import Item


@dataclass
class Phone(Item):  # Inheritance from class Item
    broken_phones: int = 0

    def __post_init__(self):
        super().__post_init__()
        assert self.broken_phones >= 0, f"Broken Phones {self.broken_phones} cannot be less than zero."
        logging.info(f"Created Phone: {self}")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.broken_phones})"
