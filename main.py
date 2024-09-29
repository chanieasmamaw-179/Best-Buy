from product import Product, Electronics, Clothing
from product import (
    PercentageDiscountPromotion, BuyOneGetOnePromotion, FixedAmountDiscountPromotion
)
from store import Store


def list_products(store: Store):
    """Lists all active products in the store."""
    products = store.get_all_products()
    if not products:
        print("No active products in the store.")
    else:
        for product in products:
            print(product.__str__())


def show_total_quantity(store: Store):
    """Shows the total quantity of all products in the store."""
    total_quantity = store.get_total_quantity()
    print(f"Total quantity in store: {total_quantity}")


def make_order(store: Store):
    """Allows the user to place an order by selecting products by ID."""
    shopping_list = []

    # Display available products with IDs
    print("Available products:")
    for idx, product in enumerate(store.get_all_products(), start=1):
        print(f"ID: {idx}, Name: {product.name}, Price: ${product.price}, Quantity Available: {product.quantity}")

    while True:
        product_id = input("Enter product ID (or type 'done' to finish): ")
        if product_id.lower() == 'done':
            break

        try:
            product_id = int(product_id)
            if product_id < 1 or product_id > len(store.get_all_products()):
                print("Invalid product ID. Please try again.")
                continue
            quantity = int(input("Enter quantity: "))

            # Fetch the selected product
            product = store.get_all_products()[product_id - 1]
            if quantity > product.quantity:
                print(f"Only {product.quantity} available for {product.name}. Try again.")
                continue

            shopping_list.append((product, quantity))
        except ValueError:
            print("Invalid input. Please enter numeric values for product ID and quantity.")

    if shopping_list:
        try:
            total_price = store.order(shopping_list)
            print(f"Total price of the order: ${total_price:.2f}")
        except ValueError as e:
            print(f"Error: {e}")
    else:
        print("No items added to the shopping list.")


def main():
    """Main function to setup the store and manage store menu."""
    # Setup initial stock of inventory and apply promotions directly during creation
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
        Product("Windows License", price=125, quantity=10),
        Product("Shipping", price=10, quantity=250),
    ]

    # Apply promotions directly on product creation
    product_list[0].set_promotion(
        PercentageDiscountPromotion(product_list[0], quantity=1, discount_percentage=25))  # 25% off MacBook Air
    product_list[1].set_promotion(BuyOneGetOnePromotion(product_list[1]))  # Buy One Get One for Bose Earbuds
    product_list[2].set_promotion(
        FixedAmountDiscountPromotion(product_list[2], quantity=2, discount_amount=50))  # $50 off Google Pixel
    product_list[3].set_promotion(
        PercentageDiscountPromotion(product_list[3], quantity=1, discount_percentage=20))  # 20% off Windows License
    product_list[4].set_promotion(FixedAmountDiscountPromotion(product_list[4], quantity=10,
                                                               discount_amount=5))  # $5 off Shipping for 10 units or more

    # Create the store instance with the product list
    best_buy = Store(product_list)

    # Display all products in the store
    print("Products available in the store:")
    for product in best_buy.get_all_products():
        print(product.__str__())

    while True:
        print("\nStore Menu:")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            list_products(best_buy)
        elif choice == '2':
            show_total_quantity(best_buy)
        elif choice == '3':
            make_order(best_buy)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == '__main__':
    main()
