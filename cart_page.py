import random
import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    INVENTORY_ITEM = (By.CLASS_NAME, "inventory_item")
    PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_PRICE = (By.CLASS_NAME, "inventory_item_price")
    CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_link .shopping_cart_badge")

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(*self.USERNAME_FIELD).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.INVENTORY_ITEM)
        )

    def get_product_element(self, product_name):
        all_products = self.get_all_products()  # Get all products
        for product in all_products:
            name = product.find_element(By.CLASS_NAME, "inventory_item_name").text
            if name == product_name:
                return product  # Return the product element if the name matches
        return None  # Return None if no matching product is found

    def get_all_products(self):
        all_products = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        return all_products
    def get_random_products(self, count=4):
        all_products = self.get_all_products()
        if len(all_products) < count:
            return []
        return random.sample(all_products, count)

    def add_to_cart(self, product_element, expected_count=None):
        # Get product details for better debugging
        product_name = product_element.find_element(*self.PRODUCT_NAME).text

        # Find the correct add to cart button
        add_button = product_element.find_element(By.XPATH, ".//button[contains(text(), 'Add to cart')]")

        # Scroll the button into view
        self.driver.execute_script("arguments[0].scrollIntoView();", add_button)

        # Click the button using JavaScript (more reliable than standard click)
        self.driver.execute_script("arguments[0].click();", add_button)
        print(f"Added '{product_name}' to cart")

        # Wait for button text to change to "Remove"
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(
                (By.XPATH, f"//div[contains(@class, 'inventory_item')][.//div[text()='{product_name}']]//button"),
                "Remove"
            )
        )

        # Verify cart count updates if expected_count is provided
        if expected_count is not None:
            try:
                WebDriverWait(self.driver, 10).until(
                    lambda d: self.get_cart_count() == expected_count
                )
            except TimeoutException:
                current_count = self.get_cart_count()
                print(f"Timeout: Expected cart count {expected_count}, but got {current_count}")
                raise
    def get_cart_count(self):
        try:
            badge = self.driver.find_element(*self.CART_BADGE)
            return int(badge.text)
        except:
            return 0

    def get_product_name_price(self, product_element):
        name = product_element.find_element(*self.PRODUCT_NAME).text
        price = product_element.find_element(*self.PRODUCT_PRICE).text
        return name, price
