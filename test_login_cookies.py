from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Save cookies from login
def login_get_cookies():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID,"user-name").send_keys("standard_user")
    driver.find_element(By.ID,"password").send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()

    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,"inventory_list")))
    cookies = driver.get_cookies()  #capture cookies after login
    driver.quit()
    return cookies

#use cookies to access logged-in page directly.
def test_login_using_cookies():
    cookies = login_get_cookies()
    driver = webdriver.Chrome()
    #Step 1:
    driver.get("https://www.saucedemo.com/") #First visit to set domain
    driver.delete_all_cookies()
    #Step 2: Add te cookies from the previous session
    for cookie in cookies:
        driver.add_cookie(cookie)

    #Step 3: Navigate directly to the protected page(after cookie injection)
    driver.get("https://www.saucedemo.com/inventory.html")
    try:
        #Wait for an element that exists only on the dashboard
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,"inventory_list")))
        print("Login successful using cookies.")

    except:
        print("Login failed using cookies.")
        assert False, "Dashboard element not found"
    finally:
        driver.quit()