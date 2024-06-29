from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# URL of the login page
url = "http://localhost/Online-Food-Ordering-System-in-PHP/login.php"

# Define test data for login functionality
test_cases = [
    {"id": "TC_LOGIN_001", "username": "alifibrahim", "password": "alif1234", "expected_result": "Successful login"},
    {"id": "TC_LOGIN_002", "username": "alifibrahim", "password": "!@#$%^&*", "expected_result": "Invalid Username or Password!"},
    {"id": "TC_LOGIN_003", "username": "alifibrahim", "password": "Alif", "expected_result": "Invalid Username or Password!"},
    {"id": "TC_LOGIN_004", "username": "alifibrahim", "password": " ", "expected_result": "Invalid Username or Password!"},
    {"id": "TC_LOGIN_005", "username": "alifibrahim", "password": "1234567", "expected_result": "Invalid Username or Password!"},
    {"id": "TC_LOGIN_006", "username": "Alif Ibrahim", "password": "alif1234", "expected_result": "Invalid Username or Password!"},
    {"id": "TC_LOGIN_007", "username": "!@#$%^&*", "password": "alif1234", "expected_result": "Invalid Username or Password!"},
    {"id": "TC_LOGIN_008", "username": " ", "password": "alif1234", "expected_result": "Invalid Username or Password!"},
    {"id": "TC_LOGIN_009", "username": "Alif Ibrahim", "password": "alif", "expected_result": "Invalid Username or Password!"},
    {"id": "TC_LOGIN_010", "username": "Alif Ibrahim", "password": "alif", "expected_result": "Invalid Username or Password!"},
    {"id": "TC_LOGIN_011", "username": "Alif Ibrahim", "password": "alif", "expected_result": "Invalid Username or Password!"},
    {"id": "TC_LOGIN_012", "username": "Alif Ibrahim", "password": "alif", "expected_result": "Invalid Username or Password!"},
    {"id": "TC_LOGIN_013", "username": "!@#$%^&*", "password": "alif", "expected_result": "Invalid Username or Password!"},
    {"id": "TC_LOGIN_014", "username": "!@#$%^&*", "password": "alif", "expected_result": "Invalid Username or Password!"},
    {"id": "TC_LOGIN_015", "username": "!@#$%^&*", "password": "alif", "expected_result": "Invalid Username or Password!"},
    {"id": "TC_LOGIN_016", "username": "!@#$%^&*", "password": "alif", "expected_result": "Invalid Username or Password!"},
    {"id": "TC_LOGIN_017", "username": "!@#$%^&*", "password": "alif", "expected_result": "Invalid Username or Password!"},
    {"id": "TC_LOGIN_018", "username": "!@#$%^&*", "password": "alif", "expected_result": "Invalid Username or Password!"},
    {"id": "TC_LOGIN_019", "username": "!@#$%^&*", "password": "alif", "expected_result": "Invalid Username or Password!"},
    {"id": "TC_LOGIN_020", "username": "!@#$%^&*", "password": "alif", "expected_result": "Invalid Username or Password!"},
    {"id": "TC_LOGIN_021", "username": "", "password": "alif1234", "expected_result": "Invalid Username or Password!"},
    {"id": "TC_LOGIN_022", "username": "alifibrahim", "password": "", "expected_result": "Invalid Username or Password!"},
    {"id": "TC_LOGIN_023", "username": "", "password": "", "expected_result": "Invalid Username or Password!"},
]

# Iterate over test cases
for test_case in test_cases:
    # Open the login page
    driver.get(url)
    # Wait for the page to load
    time.sleep(3)

    # Fill the form with test data
    driver.find_element(By.NAME, "username").clear()
    driver.find_element(By.NAME, "username").send_keys(test_case["username"])

    driver.find_element(By.NAME, "password").clear()
    driver.find_element(By.NAME, "password").send_keys(test_case["password"])

    # Click the "Login" button
    driver.find_element(By.ID, "buttn").click()

    # Wait for the result message to appear
    try:
        message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Invalid Username or Password!') or contains(text(), 'Successful login')]"))
        )

        if test_case["expected_result"] in message.text:
            print(f"Test case {test_case['id']}: PASS")
        else:
            print(f"Test case {test_case['id']}: FAIL - Unexpected message")
    except Exception as e:
        error_message = str(e).split("\n")[0]
        print(f"Test case {test_case['id']}: FAIL - Error: {error_message}")

# Close the driver
driver.quit()
