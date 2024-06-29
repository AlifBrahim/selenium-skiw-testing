from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Define test data for add restaurant category functionality
test_cases = [
    {"id": "TC_RESTAURANT_CATEGORY_001", "category": "Western", "expected_result": "Successful"},
    {"id": "TC_RESTAURANT_CATEGORY_002", "category": "abc123", "expected_result": "Unsuccessful"},
    {"id": "TC_RESTAURANT_CATEGORY_003", "category": "$", "expected_result": "Unsuccessful"},
    {"id": "TC_RESTAURANT_CATEGORY_004", "category": "123", "expected_result": "Unsuccessful"},
    {"id": "TC_RESTAURANT_CATEGORY_005", "category": " ", "expected_result": "Unsuccessful"},
]

# URL of the page to test
url = "http://localhost/Online-Food-Ordering-System-in-PHP/admin/add_category.php"

# Function to log in (assuming login is required before adding category)
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
    # Open the add category page
    driver.get(url)
    # Wait for the page to load
    time.sleep(3)

    # Fill the form with test data
    category_input = driver.find_element(By.NAME, "c_name")
    category_input.clear()
    category_input.send_keys(test_case["category"])

    # Click "Save" button
    driver.find_element(By.CSS_SELECTOR, "input[type='submit'][value='Save']").click()

    # Wait for the result message to appear
    try:
        alert = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'alert')]"))
        )

        alert_text = alert.text
        if test_case["expected_result"] == "Successful":
            if "New Category Added Successfully." in alert_text:
                print(f"Test case {test_case['id']}: PASS")
            else:
                print(f"Test case {test_case['id']}: FAIL - Success message not found")
        else:
            if "field Required!" in alert_text or "Category already exist!" in alert_text:
                print(f"Test case {test_case['id']}: PASS")
            else:
                print(f"Test case {test_case['id']}: FAIL - Error message not found")
    except Exception as e:
        error_message = str(e).split("\n")[0]
        print(f"Test case {test_case['id']}: FAIL - Error: {error_message}")

# Close the driver
driver.quit()
