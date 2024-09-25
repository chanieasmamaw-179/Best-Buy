from abc import ABC, abstractmethod


class Product:
    def __init__(self, name: str, price: float, quantity: int):
        if not name:
            raise ValueError("Product name cannot be empty")
        if price < 0:
            raise ValueError("Price cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion = None  # Initialize promotion to None

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity: int):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        return self.active

    def deactivate(self):
        self.active = False

    def __str__(self) -> str:
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def purchase(self, quantity: int):
        """Purchase a certain quantity of the product, reducing the stock."""
        if quantity > self.quantity:
            raise ValueError("Not enough stock")
        self.set_quantity(self.quantity - quantity)

    def set_promotion(self, promotion):
        """Set a promotion for the product."""
        self.promotion = promotion

    def apply_promotion(self, quantity: int) -> float:
        """Apply the promotion to the product if it exists."""
        if self.promotion:
            return self.promotion.apply_promotion(quantity)
        return self.price * quantity  # No promotion applied

    # Magic method for less than (<) comparison
    def __lt__(self, other):
        if not isinstance(other, Product):
            raise ValueError("Can only compare Product objects")
        return self.price < other.price

    # Magic method for greater than (>) comparison
    def __gt__(self, other):
        if not isinstance(other, Product):
            raise ValueError("Can only compare Product objects")
        return self.price > other.price

    # Optional: You can also add __eq__ to compare equality of prices
    def __eq__(self, other):
        if not isinstance(other, Product):
            raise ValueError("Can only compare Product objects")
        return self.price == other.price


# New Electronics class inheriting from Product
class Electronics(Product):
    def __init__(self, name: str, price: float, quantity: int, warranty: int):
        super().__init__(name, price, quantity)
        self.warranty = warranty  # warranty in months

    def __str__(self) -> str:
        return (f"{self.name} (Electronics), Price: {self.price}, "
                f"Quantity: {self.quantity}, Warranty: {self.warranty} months")


# New Clothing class inheriting from Product
class Clothing(Product):
    def __init__(self, name: str, price: float, quantity: int,
                 size: str, fabric: str):
        super().__init__(name, price, quantity)
        self.size = size
        self.fabric = fabric

    def __str__(self) -> str:
        return (f"{self.name} (Clothing), Price: {self.price}, "
                f"Quantity: {self.quantity}, Size: {self.size}, "
                f"Fabric: {self.fabric}")


# Abstract class Promotion
class Promotion(ABC):
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity

    @abstractmethod
    def apply_promotion(self) -> float:
        pass


# Derived class for percentage discount promotion
class PercentageDiscountPromotion(Promotion):
    def __init__(self, product: Product, quantity: int,
                 discount_percentage: float):
        super().__init__(product, quantity)
        self.discount_percentage = discount_percentage

    def apply_promotion(self) -> float:
        total_price = self.product.price * self.quantity
        discount_amount = total_price * (self.discount_percentage / 100)
        return total_price - discount_amount


# Derived class for buy one get one free promotion
class BuyOneGetOnePromotion(Promotion):
    def __init__(self, product: Product):
        super().__init__(product, 0)  # Quantity not needed here

    def apply_promotion(self) -> float:
        if self.product.get_quantity() < 2:
            return self.product.price * self.product.get_quantity()
        return (self.product.price *
                (self.product.get_quantity() // 2 +
                 self.product.get_quantity() % 2))


# Derived class for fixed amount discount promotion
class FixedAmountDiscountPromotion(Promotion):
    def __init__(self, product: Product, quantity: int,
                 discount_amount: float):
        super().__init__(product, quantity)
        self.discount_amount = discount_amount

    def apply_promotion(self) -> float:
        total_price = self.product.price * self.quantity
        return max(0, total_price - self.discount_amount)  # Ensure no negative
