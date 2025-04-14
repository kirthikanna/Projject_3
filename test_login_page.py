
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_swag_lab(driver):
    driver.get("https://www.saucedemo.com/")
    username = driver.find_element(By.ID,"user-name")
    username.send_keys("guvi_user")
    password = driver.find_element(By.ID,"password")
    password.send_keys("secret@123")
    login = driver.find_element(By.ID,"login-button")
    login.click()

    try:
        #Check error message
        error_message = WebDriverWait(driver,15).until(EC.visibility_of_element_located((By.XPATH,"//h3[@data-test='error']")))
        assert "Epic sadface: Username and password do not match any user in this service" in error_message.text
        print("TEST PASSED: Login failed as expected with invalid credentials.")

    except:
        print("TEST FAILED: Login should have failed,but it didn't")
        assert False, "Error message not found for invalid login"
    finally:
        driver.quit()