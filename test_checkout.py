import time
import pytest
from Pages.inventory_page import InventorPage
from Pages.cart_page import InventoryPage
from Pages.cart_button import CartButton
from Pages.checkout_page import CheckoutPage
def test_complete_checkout(driver):
    driver.get("https://www.saucedemo.com/")
    # Login
    inventory = InventoryPage(driver)
    inventory.enter_username("standard_user")
    inventory.enter_password("secret_sauce")
    inventory.click_login()

    #Add items to cart
    all_items = inventory.get_all_products()
    inventory.add_to_cart(all_items[0])
    inventory.add_to_cart(all_items[1])
    inventory.add_to_cart(all_items[2])
    inventory.add_to_cart(all_items[3])

    #Navigate to cart
    cart = CartButton(driver)
    cart.navigate_to_cart()
    print("Cart page URL:", driver.current_url)

    #checkout Page
    checkout = CheckoutPage(driver)
    checkout.click_checkout()
    print("Current URL:", driver.current_url)
    assert "checkout-step-one.html" in driver.current_url

    checkout.enter_checkout_info("Keerthana","Suresh","600001")
    checkout.click_continue()

    #Screenshot checkout overview
    time.sleep(2)
    screenshot_path = "Screenshots/checkout_overview.png"
    checkout.checkout_overview_screenshot(path=screenshot_path)
    print(f"\n Screenshot saved to :{screenshot_path}")

    #Finish checkout
    checkout.click_finish()
    confirmation_text = checkout.get_confirmation_text()
    print(f"\n Confirmation : {confirmation_text}")

    #Assertion
    assert "Thank you" in confirmation_text


