from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Define test data for add to cart functionality
test_cases = [
    {"id": "TC_ADD_TO_CART_001", "quantity": "2", "expected_result": "Successful add item to cart"},
    {"id": "TC_ADD_TO_CART_002", "quantity": "f", "expected_result": "Unsuccessful add item to cart"},
    {"id": "TC_ADD_TO_CART_003", "quantity": "f2", "expected_result": "Unsuccessful add item to cart"},
    {"id": "TC_ADD_TO_CART_004", "quantity": "2 3", "expected_result": "Unsuccessful add item to cart"},
    {"id": "TC_ADD_TO_CART_005", "quantity": "&", "expected_result": "Unsuccessful add item to cart"},
    {"id": "TC_ADD_TO_CART_006", "quantity": " ", "expected_result": "Unsuccessful add item to cart"},
    # Add more test cases here...
]

# URL of the page to test
url = "http://localhost/Online-Food-Ordering-System-in-PHP/dishes.php?res_id=1"

# Function to log in (assuming login is required before adding to cart)
def login():
    driver.get("http://localhost/Online-Food-Ordering-System-in-PHP/login.php")
    time.sleep(3)
    driver.find_element(By.NAME, "username").send_keys("user1")
    driver.find_element(By.NAME, "password").send_keys("1234567")
    driver.find_element(By.NAME, "submit").click()
    time.sleep(3)

# Log in first
login()

# Iterate over test cases
for test_case in test_cases:
    # Open the add to cart page
    driver.get(url)
    # Wait for the page to load
    time.sleep(3)

    # Find quantity input field and fill it with test data
    quantity_input = driver.find_element(By.NAME, "quantity")
    quantity_input.clear()
    quantity_input.send_keys(test_case["quantity"])

    # Click "Add To Cart" button
    driver.find_element(By.CSS_SELECTOR, "input[type='submit'][value='Add To Cart']").click()

    # Wait for the result
    time.sleep(3)

    # Check the result
    try:
        # Check the cart content
        cart_total_element = driver.find_element(By.XPATH, "//h3[@class='value']/strong")
        cart_total = cart_total_element.text.strip('$')

        if test_case["expected_result"] == "Successful add item to cart":
            if float(cart_total) > 0:
                print(f"Test case {test_case['id']}: PASS")
            else:
                print(f"Test case {test_case['id']}: FAIL")
        else:
            if float(cart_total) == 0:
                print(f"Test case {test_case['id']}: PASS")
            else:
                print(f"Test case {test_case['id']}: FAIL")

    except Exception as e:
        error_message = str(e).split("\n")[0]
        print(f"Test case {test_case['id']}: FAIL - Error: {error_message}")

# Close the driver
driver.quit()
