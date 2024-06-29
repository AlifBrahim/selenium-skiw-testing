from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Define test data for edit user functionality
test_cases = [
    {"id": "TC_EDIT_USER_001", "username": "alifibrahim", "fname": "Muhammad", "lname": "Alif",
     "email": "alif@gmail.com", "phone": "1384728439", "password": "alif1234", "expected_result": "Successful"},
    {"id": "TC_EDIT_USER_002", "username": "&^*(&&(*^(", "fname": "Muhammad", "lname": "Alif",
     "email": "alif@gmail.com", "phone": "1384728439", "password": "alif1234", "expected_result": "Unsuccessful"},
    {"id": "TC_EDIT_USER_003", "username": "alif ibrahim", "fname": "Muhammad", "lname": "Alif",
     "email": "alif@gmail.com", "phone": "1384728439", "password": "alif1234", "expected_result": "Unsuccessful"},
    {"id": "TC_EDIT_USER_004", "username": " ", "fname": "Muhammad", "lname": "Alif",
     "email": "alif@gmail.com", "phone": "1384728439", "password": "alif1234", "expected_result": "Unsuccessful"},
    {"id": "TC_EDIT_USER_005", "username": "alifibrahim", "fname": "M7hammad", "lname": "Alif",
     "email": "alif@gmail.com", "phone": "1384728439", "password": "alif1234", "expected_result": "Unsuccessful"},
    {"id": "TC_EDIT_USER_006", "username": "alifibrahim", "fname": "Muhammad", "lname": "Alif",
     "email": "alif@gmail.com", "phone": "1384728439", "password": "alif1234", "expected_result": "Successful", "cancel": True},
    {"id": "TC_EDIT_USER_007", "username": "alifibrahim", "fname": "Muhammad", "lname": "!@#$%^&*",
     "email": "alif@gmail.com", "phone": "1384728439", "password": "alif1234", "expected_result": "Unsuccessful"},
    {"id": "TC_EDIT_USER_008", "username": "alifibrahim", "fname": "Muhammad", "lname": "Alif", "email": "alifibrahim",
     "phone": "1384728439", "password": "alif1234", "expected_result": "Unsuccessful"},
    {"id": "TC_EDIT_USER_009", "username": "alifibrahim", "fname": "Muhammad", "lname": "Alif",
     "email": "alif@gmail.com", "phone": "abc123", "password": "alif1234", "expected_result": "Unsuccessful"},
    {"id": "TC_EDIT_USER_010", "username": "alifibrahim", "fname": "Muhammad", "lname": "123",
     "email": "alif@gmail.com", "phone": "1384728439", "password": "alif1234", "expected_result": "Unsuccessful"},
    {"id": "TC_EDIT_USER_011", "username": "alifibrahim", "fname": "Muhammad", "lname": " ",
     "email": "alif@gmail.com", "phone": "1384728439", "password": "alif1234", "expected_result": "Unsuccessful"},
    {"id": "TC_EDIT_USER_012", "username": "alifibrahim", "fname": "M7hammad", "lname": "Alif",
     "email": "alif@gmail.com", "phone": "1384728439", "password": "alif1234", "expected_result": "Successful", "cancel": True},
    {"id": "TC_EDIT_USER_013", "username": "alifibrahim", "fname": "Muhammad", "lname": "!@#$%^&*",
     "email": "alif@gmail.com", "phone": "1384728439", "password": "alif1234", "expected_result": "Successful", "cancel": True},
    {"id": "TC_EDIT_USER_014", "username": "alifibrahim", "fname": "Muhammad", "lname": "123",
     "email": "alif@gmail.com", "phone": "1384728439", "password": "alif1234", "expected_result": "Successful", "cancel": True},
    {"id": "TC_EDIT_USER_015", "username": "alifibrahim", "fname": "Muhammad", "lname": " ",
     "email": "alif@gmail.com", "phone": "1384728439", "password": "alif1234", "expected_result": "Successful", "cancel": True},
    {"id": "TC_EDIT_USER_016", "username": "alifibrahim", "fname": "Muhammad", "lname": "abc123",
     "email": "alif@gmail.com", "phone": "1384728439", "password": "alif1234", "expected_result": "Unsuccessful"},
    {"id": "TC_EDIT_USER_017", "username": "alifibrahim", "fname": "Muhammad", "lname": "!@#$%^&*",
     "email": "alif@gmail.com", "phone": "1384728439", "password": "alif1234", "expected_result": "Unsuccessful"},
    {"id": "TC_EDIT_USER_018", "username": "alifibrahim", "fname": "Muhammad", "lname": "123",
     "email": "alif@gmail.com", "phone": "1384728439", "password": "alif1234", "expected_result": "Unsuccessful"},
    {"id": "TC_EDIT_USER_019", "username": "alifibrahim", "fname": "Muhammad", "lname": " ",
     "email": "alif@gmail.com", "phone": "1384728439", "password": "alif1234", "expected_result": "Unsuccessful"},
    {"id": "TC_EDIT_USER_020", "username": "alifibrahim", "fname": "Muhammad", "lname": "abc123",
     "email": "alif@gmail.com", "phone": "1384728439", "password": "alif1234", "expected_result": "Successful", "cancel": True},
]

# URL of the page to test
url = "http://localhost/Online-Food-Ordering-System-in-PHP/admin/update_users.php?user_upd=9"

# Function to log in (assuming login is required before editing user)
def login():
    driver.get("http://localhost/Online-Food-Ordering-System-in-PHP/admin/index.php")
    time.sleep(3)
    driver.find_element(By.NAME, "username").send_keys("admin")
    driver.find_element(By.NAME, "password").send_keys("1234567")
    driver.find_element(By.NAME, "submit").click()
    time.sleep(3)

# Log in first
login()

# Iterate over test cases
for test_case in test_cases:
    # Open the edit user page
    driver.get(url)
    # Wait for the page to load
    time.sleep(3)

    # Fill the form with test data
    driver.find_element(By.NAME, "uname").clear()
    driver.find_element(By.NAME, "uname").send_keys(test_case["username"])

    driver.find_element(By.NAME, "fname").clear()
    driver.find_element(By.NAME, "fname").send_keys(test_case["fname"])

    driver.find_element(By.NAME, "lname").clear()
    driver.find_element(By.NAME, "lname").send_keys(test_case["lname"])

    driver.find_element(By.NAME, "email").clear()
    driver.find_element(By.NAME, "email").send_keys(test_case["email"])

    driver.find_element(By.NAME, "phone").clear()
    driver.find_element(By.NAME, "phone").send_keys(test_case["phone"])

    driver.find_element(By.NAME, "password").clear()
    driver.find_element(By.NAME, "password").send_keys(test_case["password"])

    if "cancel" in test_case and test_case["cancel"]:
        # Click "Cancel" button
        driver.find_element(By.CLASS_NAME, "btn-inverse").click()
        time.sleep(3)
        # Check if no alert is present
        try:
            WebDriverWait(driver, 3).until(
                EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'alert')]"))
            )
            print(f"Test case {test_case['id']}: FAIL - Unexpected alert found")
        except:
            print(f"Test case {test_case['id']}: PASS")
    else:
        # Click "Save" button
        driver.find_element(By.CSS_SELECTOR, "input[type='submit'][value='Save']").click()
        # Wait for the result message to appear
        try:
            alert = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'alert')]"))
            )

            alert_text = alert.text
            if test_case["expected_result"] == "Successful":
                if "User Updated!" in alert_text:
                    print(f"Test case {test_case['id']}: PASS")
                else:
                    print(f"Test case {test_case['id']}: FAIL")
            else:
                if "All fields Required!" in alert_text or "invalid email!" in alert_text or "Password must be >=6!" in alert_text or "invalid phone!" in alert_text:
                    print(f"Test case {test_case['id']}: PASS")
                else:
                    print(f"Test case {test_case['id']}: FAIL")
        except Exception as e:
            error_message = str(e).split("\n")[0]
            print(f"Test case {test_case['id']}: FAIL - Error: {error_message}")

# Close the driver
driver.quit()
