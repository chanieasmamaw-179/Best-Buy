# products.py
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

    def show(self) -> str:
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def purchase(self, quantity: int):
        """Purchase a certain quantity of the product, reducing the stock."""
        if quantity > self.quantity:
            raise ValueError("Not enough stock")
        self.set_quantity(self.quantity - quantity)


# New Electronics class inheriting from Product
class Electronics(Product):
    def __init__(self, name: str, price: float, quantity: int, warranty: int):
        super().__init__(name, price, quantity)
        self.warranty = warranty  # warranty in months

    def show(self) -> str:
        return f"{self.name} (Electronics), Price: {self.price}, Quantity: {self.quantity}, Warranty: {self.warranty} months"


# New Clothing class inheriting from Product
class Clothing(Product):
    def __init__(self, name: str, price: float, quantity: int, size: str, fabric: str):
        super().__init__(name, price, quantity)
        self.size = size
        self.fabric = fabric

    def show(self) -> str:
        return f"{self.name} (Clothing), Price: {self.price}, Quantity: {self.quantity}, Size: {self.size}, Fabric: {self.fabric}"
