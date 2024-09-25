from product import Product
from typing import List, Tuple


class Store:
    def __init__(self, products=None):
        """Initialize Store with an optional list of Product instances."""
        if products is None:
            products = []
        self.products = products

    def add_product(self, product: Product):
        """Adds a Product to the store's inventory."""
        if not isinstance(product, Product):
            raise TypeError("Expected an instance of Product")
        self.products.append(product)
        print(f"Added product: {product.name}")

    def remove_product(self, product: Product):
        """Removes a Product from the store's inventory."""
        if not isinstance(product, Product):
            raise TypeError("Expected an instance of Product")
        if product in self.products:
            self.products.remove(product)
            print(f"Removed product: {product.name}")
        else:
            print(f"Product '{product.name}' not found in store.")

    def get_total_quantity(self) -> int:
        """Returns the total quantity of all products in the store."""
        total_quantity = sum(
            product.get_quantity() for product in self.products
        )
        return total_quantity

    def get_all_products(self) -> List[Product]:
        """Returns a list of all active products in the store."""
        active_products = [
            product for product in self.products if product.is_active()
        ]
        return active_products

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        """Processes an order and returns the total price of the order."""
        total_price = 0.0

        for product, quantity in shopping_list:
            if not isinstance(product, Product):
                raise TypeError("Expected an instance of Product")
            if quantity < 0:
                raise ValueError("Quantity cannot be negative")
            if quantity > product.get_quantity():
                raise ValueError(
                    f"Not enough stock for {product.name}. "
                    f"Requested: {quantity}, "
                    f"Available: {product.get_quantity()}"
                )

            # Deduct the quantity and update total price
            product.set_quantity(product.get_quantity() - quantity)
            total_price += product.price * quantity

        print(f"Total price of the order: ${total_price:.2f}")
        return total_price

    def show_products(self) -> str:
        """Returns a string representation of all products in the store."""
        return "\n".join(product.show() for product in self.products)

    def __contains__(self, product: Product) -> bool:
        """Check if a product exists in the store using the 'in' operator."""
        return product in self.products


# Ensure this code only runs when the script is executed directly
if __name__ == '__main__':
    # Example usage for testing purposes
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)
    store = Store([bose, mac])

    # Add and remove products for testing
    store.add_product(Product("Google Pixel 7", price=500, quantity=250))
    store.remove_product(mac)

    # Check if a product is in the store using the 'in' operator
    print(bose in store)  # Output: True
    print(mac in store)   # Output: False (after removal)

    store.order([(bose, 1), (bose, 2)])
    print(store.show_products())
