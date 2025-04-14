import pytest

from Pages.inventory_page import InventorPage

def test_random_product_selection(driver):
    try:
        driver.get("https://www.saucedemo.com/")
        inventory = InventorPage(driver)
        inventory.enter_username("standard_user")
        inventory.enter_password("secret_sauce")
        inventory.click_login()
        print("Clicked login")

        selected_products = inventory.get_random_products()
        """pytest.fail() function is a built-in Pytest method used to explicitly mark a test as failed and optionally provide a message explaining why.."""
        if not selected_products:
            pytest.fail("No products returned.Either less than 4 products are available or there was an error.")
        print("\nRandomly Selected Products:")
        for name,price in selected_products:
            print(f"{name} - {price}")
        assert len(selected_products) == 4,"Did not get 4 Products"

    except Exception as e:
        print(f"Unexpected error occurred: {e}")
        raise