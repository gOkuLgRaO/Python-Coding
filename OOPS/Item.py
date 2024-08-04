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

    def __post_init__(self):
        assert self.price >= 0, f"Price {self.price} must be greater than or equal to zero."
        assert self._quantity >= 0, f"Quantity {self._quantity} must be greater than or equal to zero."
        self.__name = self.name
        self.__price = self.price
        self.__quantity = self._quantity
        Item.store_list.append(self)
        logging.info(f"Created Item: {self}")

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        if len(value) > 10:
            raise ValueError("The name is too long!")
        self.__name = value

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value: float):
        if value < 0:
            raise ValueError("Price cannot be negative!")
        self.__price = value

    @property
    def quantity(self) -> int:
        return self.__quantity

    @quantity.setter
    def quantity(self, value: int):
        if value < 0:
            raise ValueError("Quantity cannot be negative!")
        self.__quantity = value

    def apply_discount(self):
        self.__price *= self.pay_rate
        logging.info(f"Applied discount to {self.name}, new price is {self.__price}")

    def apply_increment(self, increment_value: float):
        self.__price += self.__price * increment_value
        logging.info(f"Applied increment to {self.name}, new price is {self.__price}")

    def calculate_total_price(self) -> float:
        total = self.__price * self.__quantity
        logging.info(f"Total price for {self.name} is {total}")
        return total

    @classmethod
    def instantiate_from_csv(cls, file_path: str):
        try:
            with open(file_path, 'r') as f:
                reader = csv.DictReader(f)
                items = list(reader)

            for item in items:
                cls(
                    name=item['name'],
                    price=float(item['price']),
                    _quantity=int(item['quantity'])
                )
            logging.info(f"Instantiated items from {file_path}")

        except Exception as e:
            logging.error(f"Failed to instantiate items from CSV. Error: {e}")
            raise RuntimeError(f"Failed to instantiate items from CSV. Error: {e}")

    @staticmethod
    def is_integer(num: Union[int, float]) -> bool:
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        return False

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.__quantity})"

    @staticmethod
    def __connect(smtp_server: str):
        # Dummy connection method for sending email
        logging.info(f"Connecting to {smtp_server}")

    def send_email(self):
        self.__connect('smtp.server.com')
        body = self.__prepare_body()
        self.__send(body)
        logging.info(f"Sent email for {self.name}")

    def __prepare_body(self) -> str:
        return f"""
        Hello. We have {self.name} {self.__quantity} times.
        """

    @staticmethod
    def __send(body: str):
        # Dummy send method
        logging.info(f"Sending email with body: {body}")
