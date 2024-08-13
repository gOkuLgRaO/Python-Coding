import logging
from dataclasses import dataclass, field
from datetime import datetime
from OOPS.Item import Item


@dataclass
class Phone(Item):
    broken_phones: int = 0
    year_of_manufacture: int = field(default_factory=lambda: datetime.now().year)
    battery_life: float = 100.0
    usage_hours: float = 0.0

    def __post_init__(self):
        super().__post_init__()
        assert (
            self.broken_phones >= 0
        ), f"Broken Phones {self.broken_phones} cannot be less than zero."
        assert (
            self.year_of_manufacture > 2000
        ), f"Year of manufacture {self.year_of_manufacture} is unrealistic."
        assert (
            0 <= self.battery_life <= 100
        ), f"Battery life {self.battery_life} must be between 0 and 100."
        self.update_battery_life()
        logging.info(f"Created Phone: {self}")

    # Method to update battery life based on usage
    def update_battery_life(self):
        self.battery_life -= (
            self.usage_hours * 0.1
        )  # Reduce battery life based on usage
        if self.battery_life < 0:
            self.battery_life = 0
        logging.info(
            f"Updated battery life for {self.name}, new battery life is {self.battery_life}"
        )

    # Method to calculate depreciation based on the age of the phone
    def calculate_depreciation(self) -> float:
        age = datetime.now().year - self.year_of_manufacture
        depreciation = self.price * (age * 0.1)
        if depreciation > self.price:
            depreciation = self.price
        logging.info(f"Depreciation for {self.name} is {depreciation}")
        return depreciation

    # Method to calculate the resale value after depreciation
    def calculate_resale_value(self) -> float:
        depreciation = self.calculate_depreciation()
        resale_value = self.price - depreciation
        logging.info(f"Resale value for {self.name} is {resale_value}")
        return resale_value

    # Method to check if the phone is outdated
    def is_outdated(self) -> bool:
        return datetime.now().year - self.year_of_manufacture > 3

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.broken_phones},"
            f" {self.year_of_manufacture}, {self.battery_life}, {self.usage_hours})"
        )
