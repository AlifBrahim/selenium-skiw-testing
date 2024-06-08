from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Define test data
test_cases = [
    {"id": "TC_SIGN_UP_001", "username": "alifibrahim", "firstname": "Muhammad", "lastname": "Alif", "email": "alif@gmail.com", "phone": "1384728439", "password": "alif1234", "cpassword": "alif1234", "address": "No.11, Sisiran Sintok", "expected_result": "login.php"},
    {"id": "TC_SIGN_UP_002", "username": "&*(*^&^)", "firstname": "Muhammad", "lastname": "Alif", "email": "alif2@gmail.com", "phone": "1384728439", "password": "alif1234", "cpassword": "alif1234", "address": "No.11, Sisiran Sintok", "expected_result": "registration.php"},
    {"id": "TC_SIGN_UP_003", "username": "alif ibrahim", "firstname": "Muhammad", "lastname": "Alif", "email": "alif3@gmail.com", "phone": "1384728439", "password": "alif1234", "cpassword": "alif1234", "address": "No.11, Sisiran Sintok", "expected_result": "registration.php"},
    {"id": "TC_SIGN_UP_004", "username": " ", "firstname": "Muhammad", "lastname": "Alif", "email": "alif4@gmail.com", "phone": "1384728440", "password": "alif1234", "cpassword": "alif1234", "address": "No.11, Sisiran Sintok", "expected_result": "registration.php"},
    {"id": "TC_SIGN_UP_005", "username": "alifibrahims", "firstname": "Mu7amad", "lastname": "Alif", "email": "alif5@gmail.com", "phone": "1384728439", "password": "alif1234", "cpassword": "alif1234", "address": "No.11, Sisiran Sintok", "expected_result": "registration.php"},
    {"id": "TC_SIGN_UP_006", "username": "alifibrahimz", "firstname": "&*(*^&^)", "lastname": "Alif", "email": "alif6@gmail.com", "phone": "1384728440", "password": "alif1234", "cpassword": "alif1234", "address": "No.11, Sisiran Sintok", "expected_result": "registration.php"},
    # Add more test cases here...
]

# Iterate over test cases
for i, test_case in enumerate(test_cases):
    # Open the registration page
    driver.get("http://localhost/Online-Food-Ordering-System-in-PHP/registration.php")
    # Wait for the page to load
    time.sleep(5)

    # Find form fields and fill them with test data
    driver.find_element("name", "username").send_keys(test_case["username"])
    driver.find_element("name", "firstname").send_keys(test_case["firstname"])
    driver.find_element("name", "lastname").send_keys(test_case["lastname"])
    driver.find_element("name", "email").send_keys(test_case["email"])
    driver.find_element("name", "phone").send_keys(test_case["phone"])
    driver.find_element("name", "password").send_keys(test_case["password"])
    driver.find_element("name", "cpassword").send_keys(test_case["cpassword"])
    driver.find_element("name", "address").send_keys(test_case["address"])

    # Submit the form
    driver.find_element("name", "submit").click()

    # Check the result
    try:
        # Check the current URL after the form submission
        current_url = driver.current_url
        if current_url.endswith(test_case["expected_result"]):
            print(f"Test case {test_case['id']}: PASS")
        else:
            print(f"Test case {test_case['id']}: FAIL")
    except Exception as e:
        print(f"Test case {test_case['id']}: FAIL - Error: {str(e)}")

# Close the driver
driver.quit()
