from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    #Locators
    USERNAME_FIELD = (By.ID,"user-name")
    PASSWORD_FIELD = (By.ID,"password")
    LOGIN_BUTTON = (By.ID,"login-button")
    CART_BUTTON = (By.CLASS_NAME,"shopping_cart_link")

    def __init__(self,driver):
        self.driver = driver

    def enter_username(self,username):
        self.driver.find_element(*self.USERNAME_FIELD).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def is_cart_visiible(self):
        try:
            cart = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.CART_BUTTON))
            return cart.is_displayed()
        except:
            return False
