import csv
import logging
from dataclasses import dataclass
from typing import ClassVar, List, Union

# Configure logging
logging.basicConfig(level=logging.INFO)


# noinspection PyAttributeOutsideInit
@dataclass
class Item:
    pay_rate: ClassVar[float] = 0.8  # Class attribute to give 20% discount
    store_list: ClassVar[List["Item"]] = []  # Store all instances

    name: str
    price: float
    _quantity: int = 0  # Use _quantity to avoid redeclaration issues
    _category: str = "general"
    _weight: float = 0.0
    _brand: str = "nokia"

    """
    In Python's dataclasses module, ClassVar is used to declare class variables, which are shared among all instances 
    of the class. In contrast, normal variables are instance variables, which are unique to each instance of the class.
    """

    def __post_init__(self):
        assert (
            self.price >= 0
        ), f"Price {self.price} must be greater than or equal to zero."
        assert (
            self._quantity >= 0
        ), f"Quantity {self._quantity} must be greater than or equal to zero."
        assert (
            self._weight >= 0
        ), f"Weight {self._weight} must be greater than or equal to zero"

        self.__name = self.name
        self.__price = self.price
        self.__quantity = self._quantity
        self.__category = self._category
        self.__weight = self._weight
        self.__brand = self._brand

        # we created __name, __price, __quantity etc as private variables. As, they cannot be accessed outside the class
        Item.store_list.append(self)
        logging.info(f"Created Item: {self}")

    # Now we have to generate GETTERS AND SETTERS
    @property  # GETTER for name attribute
    def name(self) -> str:
        return self.__name

    @name.setter  # SETTER FOR name attribute
    def name(self, value: str):
        if len(value) > 30:
            raise ValueError("The name is too long!")
        self.__name = value

    @property  # GETTER
    def price(self) -> float:
        return self.__price

    @price.setter  # SETTER
    def price(self, value: float):
        if value < 0:
            raise ValueError("Price cannot be negative!")
        self.__price = value

    @property  # GETTER
    def quantity(self) -> int:
        return self.__quantity

    @quantity.setter  # SETTER
    def quantity(self, value: int):
        if value < 0:
            raise ValueError("Quantity cannot be negative!")
        self.__quantity = value

    @property
    def category(self) -> str:
        return self.__category

    @category.setter
    def category(self, value: str):
        self.__category = value

    @property
    def weight(self) -> float:
        return self.__weight

    @weight.setter
    def weight(self, value: float):
        if value < 0:
            raise ValueError(f"Weight {value} cannot be negative")
        self.__weight = value

    @property
    def brand(self) -> str:
        return self.__brand

    @brand.setter
    def brand(self, value: str):
        self.__brand = value

    def apply_discount(self):
        if self.__category.lower() == "luxury":
            self.__price *= self.pay_rate * 0.9
        else:
            self.__price *= self.pay_rate
        logging.info(f"Applied discount to {self.__name}, new price is {self.__price}")

    def apply_increment(self, increment_value: float):
        self.__price += self.__price * increment_value
        logging.info(f"Applied increment to {self.__name}, new price is {self.__price}")

    def calculate_total_price(self) -> float:
        total = self.__price * self.__quantity
        total += self.__weight * 0.05
        logging.info(f"Total price for {self.__name} is {total}")
        return total

    """
    Class Methods
    Access to Class: Class methods have access to the class (cls) but not to the instance (self).
    Used for Factory Methods: They are often used for factory methods that create instances 
    of the class in a certain way.
    """

    @classmethod
    def instantiate_from_csv(cls, file_path: str):
        try:
            with open(file_path, "r") as f:
                reader = csv.DictReader(f)
                items = list(reader)

            for item in items:
                cls(
                    name=item["name"],
                    price=float(item["price"]),
                    _quantity=int(item["_quantity"]),
                    _category=item.get("_category", "general"),
                    _weight=float(item.get("_weight", 0)),
                    _brand=item.get("_brand", "generic"),
                )
            logging.info(f"Instantiated items from {file_path}")

        except Exception as e:
            logging.error(f"Failed to instantiate items from CSV. Error: {e}")
            raise RuntimeError(f"Failed to instantiate items from CSV. Error: {e}")

    """
    Static Methods
    No Access to Class or Instance: Static methods do not have access to the class (cls) or 
    instance (self) they are defined in.
    Utility Functions: They are typically used to define utility functions that do not 
    depend on class or instance-specific data.
    """

    @staticmethod
    def is_integer(num: Union[int, float]) -> bool:
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        return False

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}('{self.__name}', {self.__price}, {self.__quantity}, '{self.__category}', "
            f"{self.__weight}, '{self.__brand}')"
        )

    @staticmethod
    def __connect(smtp_server: str):
        # Dummy connection method for sending email
        logging.info(f"Connecting to {smtp_server}")

    def send_email(self):
        self.__connect("smtp.server.com")
        body = self.__prepare_body()
        self.__send(body)
        logging.info(f"Sent email for {self.__name}")

    def __prepare_body(self) -> str:
        return f"""
                Hello,

                We have {self.__name} available in our store. The current stock is {self.__quantity} units.

                Price: ${self.__price}
                Category: {self.__category}
                Weight: {self.__weight} kg
                Brand: {self.__brand}

                Thank you for your interest in our products!
                """

    @staticmethod
    def __send(body: str):
        # Dummy send method
        logging.info(f"Sending email with body: {body}")
