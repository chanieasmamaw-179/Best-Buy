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
            return self.promotion.apply_promotion(quantity)  # Pass quantity
        return self.price * quantity  # No promotion applied


class Electronics(Product):
    def __init__(self, name: str, price: float, quantity: int, warranty: int):
        super().__init__(name, price, quantity)
        self.warranty = warranty  # warranty in months

    def __str__(self) -> str:
        return (f"{self.name} (Electronics), Price: {self.price}, "
                f"Quantity: {self.quantity}, Warranty: {self.warranty} months")


class Clothing(Product):
    def __init__(self, name: str, price: float, quantity: int, size: str, fabric: str):
        super().__init__(name, price, quantity)
        self.size = size
        self.fabric = fabric

    def __str__(self) -> str:
        return (f"{self.name} (Clothing), Price: {self.price}, "
                f"Quantity: {self.quantity}, Size: {self.size}, "
                f"Fabric: {self.fabric}")


class Promotion(ABC):
    def __init__(self, product: Product):
        self.product = product

    @abstractmethod
    def apply_promotion(self, quantity: int) -> float:
        pass


class SecondHalfPrice(Promotion):
    """Every second product is half price."""
    def apply_promotion(self, quantity: int) -> float:
        full_price_items = (quantity + 1) // 2  # First half are full price
        half_price_items = quantity // 2  # Second half are half price
        return (full_price_items * self.product.price) + (half_price_items * self.product.price * 0.5)


class ThirdOneFree(Promotion):
    """Every third product is free."""
    def apply_promotion(self, quantity: int) -> float:
        paid_items = quantity - (quantity // 3)  # Subtract every third item
        return paid_items * self.product.price


class PercentDiscount(Promotion):
    """Applies a percentage discount to the product."""
    def __init__(self, product: Product, percent: float):
        super().__init__(product)
        self.percent = percent

    def apply_promotion(self, quantity: int) -> float:
        total_price = self.product.price * quantity
        discount_amount = total_price * (self.percent / 100)
        return total_price - discount_amount
