from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    #Locators
    USERNAME_FIELD = (By.ID,"user-name")
    PASSWORD_FIELD = (By.ID,"password")
    LOGIN_BUTTON = (By.ID,"login-button")
    MENU_BUTTON = (By.ID,"react-burger-menu-btn")
    LOGOUT_BUTTON = (By.ID,"logout_sidebar_link")

    def __init__(self,driver):
        self.driver = driver

    def enter_username(self,username):
        self.driver.find_element(*self.USERNAME_FIELD).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def click_menu(self):
        self.driver.find_element(*self.MENU_BUTTON).click()

    def click_logout(self):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.LOGOUT_BUTTON)).click()


    def logout_button_visible(self):
        #Return True if logout button is visible after clicking the menu

        try:
            self.click_menu()
            logout_button = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.LOGOUT_BUTTON))
            return logout_button.is_displayed()
        except:
            return False

    def logged_in(self):
        #Check if the inventory page is loaded
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,"inventory_list")))
            return True
        except:
            return False

    def on_login_page(self):
        #check if we are on login page
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.USERNAME_FIELD))
            return True
        except:
            return False

