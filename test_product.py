import pytest
from product import Product


### Product Tests ###

def test_normal_product_creation():
    """Test that creating a normal product works."""
    product = Product("MacBook Pro", price=2000, quantity=50)
    assert product.name == "MacBook Pro"
    assert product.price == 2000
    assert product.quantity == 50
    assert product.is_active() == True


def test_invalid_product_creation():
    """Test that creating a product with invalid details raises an exception."""
    # Test empty name
    with pytest.raises(ValueError, match="Product name cannot be empty"):
        Product("", price=1450, quantity=100)

    # Test negative price
    with pytest.raises(ValueError, match="Price cannot be negative"):
        Product("MacBook Air M2", price=-10, quantity=100)


def test_product_becomes_inactive_at_zero_quantity():
    """Test that when a product reaches 0 quantity, it becomes inactive."""
    product = Product("MacBook Air M2", price=1450, quantity=100)
    product.set_quantity(0)
    assert product.get_quantity() == 0
    assert product.is_active() == False


def test_product_purchase_modifies_quantity():
    """Test that purchasing a product modifies the quantity correctly."""
    product = Product("MacBook Air M2", price=1450, quantity=10)

    # Simulate purchasing 3 units
    product.set_quantity(product.get_quantity() - 3)

    assert product.get_quantity() == 7  # 10 - 3 = 7
    assert product.is_active() == True  # Still active since quantity > 0

def test_purchase_larger_quantity_than_available():
    """Test that buying more than available quantity raises an exception."""
    product = Product("MacBook Air M2", price=1450, quantity=5)

    # Try to purchase 10 units when only 5 are available
    with pytest.raises(ValueError, match="Not enough stock"):
        product.purchase(10)
