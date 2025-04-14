from Pages.login_visible_functionality import LoginPage


def test_logout_button_visibility(driver):
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)

    # Login
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()
    print("Clicked login")

    # Assertion - inventory page loaded
    assert login_page.logged_in(), "Login failed - Inventory page not loaded"
    print("Login Successful")

    # Check logout button visibility
    assert login_page.logout_button_visible(), "Logout button not visible after clicking menu"
    print("Logout button is visible")
def test_logout_functionality(driver):
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)

    # Login
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    # Ensure logged in
    assert login_page.logged_in(), "Login failed - Inventory page not loaded"
    print("Login Successful")

    # Click logout
    login_page.click_menu()
    print("clicked menu")
    login_page.click_logout()
    print("Logout successful")
    print("Logout button is functioning")

    # Validate redirection to login page
    assert login_page.on_login_page(), "Logout failed - Not redirected to login page"
    print("Back to login page")
