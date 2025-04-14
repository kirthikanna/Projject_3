#  PAT Capstone Project: Automated Testing for SauceDemo Web Application

##  Project Overview

This project is a comprehensive **automation testing framework** built using:

-  Python  
-  Selenium WebDriver  
-  PyTest  
-  Page Object Model (POM)  
-  Data-Driven Framework (DDFT)  
-  Keyword-Driven Hybrid Testing  
-  Explicit Waits  
-  HTML Report Generation  

The system is designed to **automatically test** the functionality of the CRM demo web application hosted at [https://www.saucedemo.com/](https://www.saucedemo.com/). It validates various scenarios to ensure the correctness and consistency of UI elements and user flows.

---

##  Features

- Fully modular POM-based test framework
- DDFT for testing with multiple user credentials
- Keyword-driven automation logic
- Explicit wait usage to handle dynamic elements
- Screenshot capture on failure
- HTML report generation for test results

---

## 🧰 Tech Stack

| Tool            | Usage                               |
|-----------------|--------------------------------------|
| Python          | Programming language                |
| Selenium        | Browser automation                  |
| Pytest          | Testing framework                   |
| pytest-html     | Report generation                   |
| Chrome          | Browser for test execution          |

---

## 🧪 Test Suite Summary

### ✅ Test Case 01
- Login with multiple users (`standard_user`, `problem_user`, etc.)
- Login using cookies (without navigating to login page)
- Pytest HTML report

### ✅ Test Case 02
- Login with invalid credentials (`guvi_user`, `secret@123`)
- Report generation

### ✅ Test Case 03
- Verify logout functionality and its visibility

### ✅ Test Case 04
- Verify cart button visibility

### ✅ Test Case 05
- Randomly select 4 out of 6 products using Python
- Fetch and print product name & price

### ✅ Test Case 06
- Randomly choose and add 4 products to the cart
- Verify the cart badge count reflects 4 items

### ✅ Test Case 07
- Fetch and validate product details from the cart

### ✅ Test Case 08
- Complete the checkout form (first name, last name, ZIP)
- Take a screenshot of checkout overview
- Finish purchase and validate confirmation

---

## 🗂️ Project Structure

PAT-Capstone/
│
├── Pages/                           # POM Classes for Page Elements & Actions
│   ├── __init__.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── cart_button.py               # Optional: If cart-specific locators/actions separated
│   └── login_cart_visible.py        # Optional: If modular visibility check split
│
├── Tests/                           # All Pytest Test Cases
│   ├── __init__.py
│   ├── test_login.py
│   ├── test_login_cookies.py
│   ├── test_login_page.py
│   ├── test_inventory_page.py
│   ├── test_cart_page.py
│   ├── test_cart_contents.py
│   ├── test_cart_visible.py
│   ├── test_checkout.py
│   ├── test_functionality.py       

│   └── excel_function.py            # Read/write Excel utilities
│   ├── locators.py                  # Common locators (if reused across pages)
│   ├── explicit_waits.py            # Reusable explicit wait methods
│
├── Screenshots/                     # Captured screenshots on failure or checkouts
│   └── checkout_after_click.png
│
├── Reports/                         # PyTest HTML Reports
│   ├── report.html
│   ├── report1.html
│   ├── report2.html
│   └── report3.html                 # Remaining reports
│
├── conftest.py                      # Pytest Fixtures & Browser setup



