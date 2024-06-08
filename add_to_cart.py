from selenium import webdriver
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
    driver.find_element("name", "username").send_keys("user1")
    driver.find_element("name", "password").send_keys("1234567")
    driver.find_element("name", "submit").click()
    time.sleep(3)

# Log in first
login()

# Iterate over test cases
for i, test_case in enumerate(test_cases):
    # Open the add to cart page
    driver.get(url)
    # Wait for the page to load
    time.sleep(3)

    # Find quantity input field and fill it with test data
    quantity_input = driver.find_element("name", "quantity")
    quantity_input.clear()
    quantity_input.send_keys(test_case["quantity"])

    # Click "Add To Cart" button
    driver.find_element("css selector", "input[type='submit'][value='Add To Cart']").click()

    # Wait for the result
    time.sleep(3)

    # Check the result
    try:
        # Check the success message or error message
        if test_case["expected_result"] == "Successful add item to cart":
            success_message = driver.find_element("id", "success_message").text
            if "successfully" in success_message.lower():
                print(f"Test case {test_case['id']}: PASS")
            else:
                print(f"Test case {test_case['id']}: FAIL")
        else:
            error_message = driver.find_element("id", "error_message").text
            # if "unsuccessful" in error_message.lower() or "invalid" in error_message.lower():
            #     print(f"Test case {test_case['id']}: PASS")
            # else:
            print(f"Test case {test_case['id']}: FAIL")
    except Exception as e:
        print(f"Test case {test_case['id']}: FAIL - Error: {str(e)}")

# Close the driver
driver.quit()
