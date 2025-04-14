from itertools import product

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.cart_page import InventoryPage
from Pages.cart_button import CartButton

def test_verify_cart_contents(driver):
    # Initialize page objects
    inventory = InventoryPage(driver)
    cart = CartButton(driver)

    # Login
    driver.get("https://www.saucedemo.com/")
    inventory.enter_username("standard_user")
    inventory.enter_password("secret_sauce")
    inventory.click_login()

    # Verify login success
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_item")),
        message="Login failed or inventory not loaded"
    )

    #Add 4 random products to cart
    selected_products = inventory.get_random_products(4)
    product_details = []

    print("\nAdding products to cart:")
    for i,product in enumerate(selected_products,1):
        name,price = inventory.get_product_name_price(product)
        product_details.append({'name': name,'price':price})
        print(f"{i} .{name} - {price}")
        inventory.add_to_cart(product, expected_count=i)
        # Verify cart count before navigation
    cart_count = inventory.get_cart_count()
    assert cart_count == 4, f"Expected 4 items in cart badge, found {cart_count}"

    # Navigate to cart and verify contents
    cart_items = cart.get_cart_items()
    assert len(cart_items) == 4, f"Expected 4 items in cart, found {len(cart_items)}"

    # Print cart contents for verification
    print("\nCart Contents:")
    for i, item in enumerate(cart_items, 1):
        print(f"{i}. {item['name']} - {item['price']} (Qty: {item['quantity']})")
        print(f"   Description: {item['description']}")

        # Verify product is in our added list
        assert any(p['name'] == item['name'] for p in product_details), \
            f"Product {item['name']} not found in added products"

