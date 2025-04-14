from Pages.login_cart_visible import LoginPage

def test_cart_visiblility(driver):
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)


    try:
        # Login
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login()
        print("Clicked login")

        # Check cart button visibility
        assert login_page.is_cart_visiible(), "cart button is not visible after login"
        print("Cart button is visible")

    except Exception as e:
        print(f"unexpected error occurred: {e}")
        raise