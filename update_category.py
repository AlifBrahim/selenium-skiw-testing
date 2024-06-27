from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Define test data for update restaurant category functionality
test_cases = [
    {"id": "TC_EDIT_RESTAURANT_001", "category": "Western", "expected_result": "Successful"},
    {"id": "TC_EDIT_RESTAURANT_002", "category": "Western", "expected_result": "NotSaved", "cancel": True},
    {"id": "TC_EDIT_RESTAURANT_003", "category": "abc123", "expected_result": "Unsuccessful"},
    {"id": "TC_EDIT_RESTAURANT_004", "category": "abc123", "expected_result": "NotSaved", "cancel": True},
    {"id": "TC_EDIT_RESTAURANT_005", "category": "$", "expected_result": "Unsuccessful"},
    {"id": "TC_EDIT_RESTAURANT_006", "category": "$", "expected_result": "NotSaved", "cancel": True},
    {"id": "TC_EDIT_RESTAURANT_007", "category": "1234", "expected_result": "Unsuccessful"},
    {"id": "TC_EDIT_RESTAURANT_008", "category": "1234", "expected_result": "NotSaved", "cancel": True},
    {"id": "TC_EDIT_RESTAURANT_009", "category": " ", "expected_result": "Unsuccessful"},
    {"id": "TC_EDIT_RESTAURANT_010", "category": " ", "expected_result": "NotSaved", "cancel": True},
]

# URL of the page to test
url = "http://localhost/Online-Food-Ordering-System-in-PHP/admin/update_category.php?cat_upd=8"

# Function to log in (assuming login is required before updating category)
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
    # Open the update category page
    driver.get(url)
    # Wait for the page to load
    time.sleep(3)

    # Fill the form with test data
    category_input = driver.find_element(By.NAME, "c_name")
    category_input.clear()
    category_input.send_keys(test_case["category"])

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
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'alert')]"))
            )

            if test_case["expected_result"] == "Successful":
                try:
                    success_message = driver.find_elements(By.XPATH, "//div[contains(@class, 'alert')]")
                    if any("Updated! Successfully." or "Category already exists!" in element.text for element in success_message):
                        print(f"Test case {test_case['id']}: PASS")
                    else:
                        print(f"Test case {test_case['id']}: FAIL - Success message not found")
                except Exception as e:
                    print(f"Test case {test_case['id']}: FAIL - Error: {str(e)}")
            elif test_case["expected_result"] == "NotSaved":
                try:
                    if not any(alert.is_displayed() for alert in driver.find_elements(By.XPATH, "//div[contains(@class, 'alert')]")):
                        print(f"Test case {test_case['id']}: PASS")
                    else:
                        print(f"Test case {test_case['id']}: FAIL - Unexpected alert found")
                except Exception as e:
                    print(f"Test case {test_case['id']}: FAIL - Error: {str(e)}")
            else:
                try:
                    error_message = driver.find_element(By.CSS_SELECTOR, "div.alert.alert-danger.alert-dismissible.fade.show").text
                    if "Invalid Category Name" in error_message or "Field Required" in error_message or "Category already exists!" in error_message:
                        print(f"Test case {test_case['id']}: FAIL")
                    else:
                        print(f"Test case {test_case['id']}: FAIL - Error message not found")
                except Exception as e:
                    print(f"Test case {test_case['id']}: FAIL - Error: {str(e)}")
        except Exception as e:
            print(f"Test case {test_case['id']}: FAIL - Error: {str(e)}")

# Close the driver
driver.quit()
