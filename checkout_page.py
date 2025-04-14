from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self,driver):
        self.driver = driver
        self.checkout_button = (By.ID,"checkout")
        self.first_name_input = (By.ID,"first-name")
        self.last_name_input = (By.ID,"last-name")
        self.postal_code_input = (By.ID,"postal-code")
        self.continue_button = (By.ID,"continue")
        self.finish_button = (By.ID,"finish")
        self.confirmation_msg = (By.CLASS_NAME,"complete-header")

    def click_checkout(self):
        wait = WebDriverWait(self.driver, 10)

        try:
            checkout_button = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
            print("Checkout button is clickable")
            checkout_button.click()
            self.driver.save_screenshot("checkout_after_click.png")

            # Better than checking URL — wait for checkout form input
            wait.until(EC.presence_of_element_located((By.ID, "first-name")))
            print("Checkout form loaded")
        except Exception as e:
            print("Checkout failed:", e)
            raise


    def enter_checkout_info(self,first_name,last_name,postal_code):
        wait = WebDriverWait(self.driver,10)
        first_name_input = wait.until(EC.presence_of_element_located((By.ID,"first-name")))
        last_name_input = wait.until(EC.presence_of_element_located((By.ID,"last-name")))
        postal_code_input = wait.until(EC.presence_of_element_located((By.ID,"postal-code")))
        first_name_input.send_keys(first_name)
        last_name_input.send_keys(last_name)
        postal_code_input.send_keys(postal_code)

    def click_continue(self):
        self.driver.find_element(*self.continue_button).click()

    def checkout_overview_screenshot(self,path="checkout_overview.png"):
        self.driver.save_screenshot(path)

    def click_finish(self):
        self.driver.find_element(*self.finish_button).click()

    def get_confirmation_text(self):
        return self.driver.find_element(*self.confirmation_msg).text