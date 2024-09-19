from product import Product
from store import Store


def main():
    # Create initial products
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)
    pixel = Product("Google Pixel 7", price=500, quantity=250)

    # Print details of the products
    print(bose.show())
    print(mac.show())
    print(pixel.show())

    # Create a product list for the store
    product_list = [mac, bose, pixel]

    # Initialize the store with the product list
    store = Store(product_list)

    # Print all products and total quantity
    print("All active products:")
    for product in store.get_all_products():
        print(product.show())

    print(f"Total quantity in store: {store.get_total_quantity()}")

    # Place an order
    order_total = store.order([(product_list[0], 1), (product_list[1], 2)])
    print(f"Total price of the order: ${order_total:.2f}")

    # Print all products in the store after order
    print("Products in store after order:")
    print(store.show_products())


if __name__ == '__main__':
    main()