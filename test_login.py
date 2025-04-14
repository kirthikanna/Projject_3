import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from excel_function import ExcelReader
from locators import WebLocators
from data import Data
import time


#Read data from Excel for parametrization
def get_test_data():
    excel_reader = ExcelReader(Data().EXCEL_FILE, Data().SHEET_NUMBER)
    rows = excel_reader.row_count()
    data = []
    for row in range(2, rows + 1):
        username = excel_reader.read_data(row, 6)
        password = excel_reader.read_data(row, 7)
        data.append((row, username, password))
    return data
@pytest.mark.parametrize("row,username,password", get_test_data())
def test_login(driver,row,username,password):
    driver.get(Data().URL)

    #Wait until the username input is visible
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,WebLocators.USERNAME)))
    driver.find_element(By.ID, WebLocators.USERNAME).clear()
    driver.find_element(by=By.ID, value=WebLocators.USERNAME).send_keys(username)

    driver.find_element(By.ID, WebLocators.PASSWORD).clear()
    driver.find_element(by=By.ID, value=WebLocators.PASSWORD).send_keys(password)

    driver.find_element(by=By.ID, value=WebLocators.SUBMIT_BUTTON).click()

    """Wait for the page to load and check if the login is successful"""
    driver.implicitly_wait(10)
    excel_reader = ExcelReader(Data().EXCEL_FILE,Data().SHEET_NUMBER)
    if Data().DASHBOARD_URL in driver.current_url:
        print(f"SUCCESS : Login success with USERNAME={username} and PASSWORD={password}")
        excel_reader.write_data(row,8,"TEST PASSED")
    else:
        print(f"ERROR : Login failed with USERNAME={username} and PASSWORD={password}")
        excel_reader.write_data(row,8,"TEST FAIL")



