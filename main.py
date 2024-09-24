from product import Product, Electronics, Clothing
from store import Store

def list_products(store: Store):
    """Lists all active products in the store."""
    products = store.get_all_products()
    if not products:
        print("No active products in the store.")
    else:
        for product in products:
            print(product.show())

def show_total_quantity(store: Store):
    """Shows the total quantity of all products in the store."""
    total_quantity = store.get_total_quantity()
    print(f"Total quantity in store: {total_quantity}")

def make_order(store: Store):
    """Allows the user to place an order."""
    shopping_list = []
    while True:
        product_name = input("Enter product name (or type 'done' to finish): ")
        if product_name.lower() == 'done':
            break

        quantity = int(input(f"Enter quantity for {product_name}: "))

        # Find the product
        product = next((p for p in store.get_all_products() if p.name == product_name), None)
        if not product:
            print(f"Product '{product_name}' not found.")
            continue

        shopping_list.append((product, quantity))

    try:
        total_price = store.order(shopping_list)
        print(f"Total price of the order: ${total_price:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

def main():
    # Initialize the store with some products including Electronics and Clothing
    product_list = [
        Electronics("MacBook Air M2", price=1450, quantity=100, warranty=12),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
        Clothing("T-Shirt", price=20, quantity=300, size="M", fabric="Cotton"),
    ]

    # Create the store instance with the product list
    best_buy = Store(product_list)

    # Display all products in the store
    print("Products available in the store:")
    for product in best_buy.get_all_products():
        print(product.show())

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
