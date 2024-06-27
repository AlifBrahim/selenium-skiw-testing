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
    {"id": "TC_EDIT_USER_005", "username": "alifibrahim", "fname": "M7hammad", "lname": "Alif",
     "email": "alif@gmail.com", "phone": "1384728439", "password": "alif1234", "expected_result": "Unsuccessful"},
    {"id": "TC_EDIT_USER_007", "username": "alifibrahim", "fname": "Muhammad", "lname": "!@#$%^&*",
     "email": "alif@gmail.com", "phone": "1384728439", "password": "alif1234", "expected_result": "Unsuccessful"},
    {"id": "TC_EDIT_USER_008", "username": "alifibrahim", "fname": "Muhammad", "lname": "Alif", "email": "alifibrahim",
     "phone": "1384728439", "password": "alif1234", "expected_result": "Unsuccessful"},
    {"id": "TC_EDIT_USER_009", "username": "alifibrahim", "fname": "Muhammad", "lname": "Alif",
     "email": "alif@gmail.com", "phone": "abc123", "password": "alif1234", "expected_result": "Unsuccessful"},
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
for i, test_case in enumerate(test_cases):
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

    # Click "Save" button
    driver.find_element(By.CSS_SELECTOR, "input[type='submit'][value='Save']").click()

    # Wait for the result message to appear
    time.sleep(3)

    # Check the result
    try:
        # Wait for the alert to be visible
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'alert')]"))
        )

        # Check for success message
        if test_case["expected_result"] == "Successful":
            success_message = driver.find_element(By.CSS_SELECTOR, "div.alert.alert-success.alert-dismissible.fade.show").text
            if "User Updated Successfully!" in success_message:
                print(f"Test case {test_case['id']}: PASS")
            else:
                print(f"Test case {test_case['id']}: FAIL")
        else:
            error_message = driver.find_element(By.CSS_SELECTOR, "div.alert.alert-danger.alert-dismissible.fade.show").text
            print(f"Test case {test_case['id']}: FAIL")
    except Exception as e:
        print(f"Test case {test_case['id']}: FAIL - Error: {str(e)}")

# Close the driver
driver.quit()
