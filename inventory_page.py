import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventorPage:
    #Locators
    USERNAME_FIELD = (By.ID,"user-name")
    PASSWORD_FIELD = (By.ID,"password")
    LOGIN_BUTTON = (By.ID,"login-button")
    INVENTORY_PAGE = (By.CLASS_NAME,"inventory_list")

    def __init__(self,driver):
        self.driver = driver

    def enter_username(self,username):
        self.driver.find_element(*self.USERNAME_FIELD).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def get_random_products(self,count=4):
        try:
            #wait for all products to load
            WebDriverWait(self.driver,10).until(EC.presence_of_all_elements_located((By.CLASS_NAME,"inventory_item")))
            all_products = self.driver.find_elements(By.CLASS_NAME,"inventory_item")
            if len(all_products) < count:
                print(f"Only found {len(all_products)} products.cannot select {count}")
                return []   #return an empty listy instead of None
            selected  = random.sample(all_products,count)#Python built-in module.Picks 4 different product elements randomly for further use.
            selected_product_info = []
            for product in selected:
                name   = product.find_element(By.CLASS_NAME,"inventory_item_name ").text
                price = product.find_element(By.CLASS_NAME,"inventory_item_price").text
                selected_product_info.append((name,price))
            return selected_product_info #valid list of products
        except Exception as e:
            print(f"Error selecting random products: {e}")
            return [] #return empty list even if error occurs

