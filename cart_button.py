from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartButton:
    CART_CONTAINER = (By.ID, "cart_contents_container")
    CART_ITEM = (By.CSS_SELECTOR,".cart_item")
    CART_BUTTON = (By.CLASS_NAME, "shopping_cart_link")
    ITEM_NAME = (By.CSS_SELECTOR,".inventory_item_name")
    ITEM_PRICE = (By.CSS_SELECTOR,".inventory_item_price")
    ITEM_DESC = (By.CSS_SELECTOR,".inventory_item_desc")
    ITEM_QUANTITY = (By.CSS_SELECTOR,".cart_quantity")
    CONTINUE_SHOPPING_BUTTTON = (By.ID,"continue-shopping")
    CHECKOUT_BUTTON= (By.ID,"checkout")

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)

    def navigate_to_cart(self):
        """Clicks cart button and waits for cart page to load"""
        try:
            # Scroll cart button into view and click using JavaScript
            cart_btn = self.wait.until(
                EC.element_to_be_clickable(self.CART_BUTTON),
                message = "Cart button not clickable"
            )
            # Scroll and click using JavaScript
            self.driver.execute_script("arguments[0].scrollIntoView(true);", cart_btn)
            self.driver.execute_script("arguments[0].click();", cart_btn)

            # Wait for cart page to load
            self.wait.until(
                EC.visibility_of_element_located(self.CART_CONTAINER),
                message="Cart page did not load within 10 seconds"
            )
            return True
        except Exception as e:
            print(f"Error navigating to cart: {str(e)}")
            return False

    def get_cart_items(self):
        """Returns list of all cart items with their details"""
        if not self.navigate_to_cart():
            return []

        try:
            cart_items = self.wait.until(
                lambda d: d.find_elements(*self.CART_ITEM),
                message="No cart items found"
            )
            items = []
            for item in cart_items:
                items.append({
                    'name': item.find_element(*self.ITEM_NAME).text,
                    'price': item.find_element(*self.ITEM_PRICE).text,
                    'description': item.find_element(*self.ITEM_DESC).text,
                    'quantity': item.find_element(*self.ITEM_QUANTITY).text
                })
            return items

        except Exception as e:
            print(f"Error getting cart items: {str(e)}")
        return []

    def get_cart_item_names(self):
        """Returns list of product names in cart"""
        return [item['name'] for item in self.get_cart_item_names()]
    def continue_shopping(self):
        self.driver.find_element(*self.CONTINUE_SHOPPING_BUTTTON).click()
    def proceed_to_checkout(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()