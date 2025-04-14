import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Pages.cart_page import InventoryPage

def test_add_random_products_to_cart(driver):
    driver.get("https://www.saucedemo.com/")
    inventory = InventoryPage(driver)

    # Login
    inventory.enter_username("standard_user")
    inventory.enter_password("secret_sauce")
    inventory.click_login()

    #Get random products
    selected = inventory.get_random_products(4)
    if len(selected) !=4:
        pytest.fail(f"Expected 4 products, got {len(selected)}")

    print("\nSelected Products:")
    for i, product in enumerate(selected, start=1):
        name, price = inventory.get_product_name_price(product)
        print(f"{i}. {name} - {price}")
        inventory.add_to_cart(product, expected_count=i)
        time.sleep(3)
    #Final verification
    cart_count = inventory.get_cart_count()
    assert cart_count == 4, f"Expected 4 items, but found {cart_count}"
