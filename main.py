from product import Product, Electronics, Clothing
from product import PercentageDiscountPromotion, BuyOneGetOnePromotion, FixedAmountDiscountPromotion
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

def apply_promotions():
    """Demonstrates the application of promotions."""
    # Example of applying promotions
    product = Product("T-Shirt", price=20, quantity=10)

    # Percentage discount
    promo1 = PercentageDiscountPromotion(product, quantity=3, discount_percentage=30)
    print(f"Total after percentage discount: ${promo1.apply_promotion():.2f}")

    # Buy one get one free
    promo2 = BuyOneGetOnePromotion(product)
    print(f"Total after BOGO: ${promo2.apply_promotion():.2f}")

    # Fixed amount discount
    promo3 = FixedAmountDiscountPromotion(product, quantity=3, discount_amount=10)
    print(f"Total after fixed discount: ${promo3.apply_promotion():.2f}")

def main():
    # Setup initial stock of inventory
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
        Product("Windows License", price=125, quantity=10),  # Ensure quantity is set
        Product("Shipping", price=10, quantity=250),
    ]

    # Create promotions
    second_half_price = PercentageDiscountPromotion(product_list[0], quantity=1, discount_percentage=50)  # 50% off
    third_one_free = BuyOneGetOnePromotion(product_list[1])  # Buy one get one free
    fixed_discount = FixedAmountDiscountPromotion(product_list[2], quantity=2, discount_amount=50)  # $50 off

    # Set promotions to products
    product_list[0].set_promotion(second_half_price)  # Apply to MacBook Air
    product_list[1].set_promotion(third_one_free)     # Apply to Bose Earbuds
    product_list[2].set_promotion(fixed_discount)      # Apply to Google Pixel 7

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
        print("4. Apply promotions")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            list_products(best_buy)
        elif choice == '2':
            show_total_quantity(best_buy)
        elif choice == '3':
            make_order(best_buy)
        elif choice == '4':
            apply_promotions()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == '__main__':
    main()
