# product.py
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> float:
        return self.quantity

    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()
        print(f"Quantity set to {self.quantity}. Product active: {self.active}")

    def is_active(self) -> bool:
        return self.active

    def deactivate(self):
        self.active = False
        print(f"Product '{self.name}' has been deactivated.")

    def show(self) -> str:
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"
