from product import Product  # Import the correct class

def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)
    print(bose.show())
    print(mac.show())


if __name__ == '__main__':
    main()
