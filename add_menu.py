from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Function to log in (assuming login is required before adding a menu)
def login():
    driver.get("http://localhost/Online-Food-Ordering-System-in-PHP/admin/index.php")
    time.sleep(3)
    driver.find_element(By.NAME, "username").send_keys("admin")
    driver.find_element(By.NAME, "password").send_keys("1234567")
    driver.find_element(By.NAME, "submit").click()
    time.sleep(3)

# Log in first
login()

# URL of the add menu page
url = "http://localhost/Online-Food-Ordering-System-in-PHP/admin/add_menu.php"

# Define test data for adding a menu
test_cases = [
    {"id": "TC_ADD_MENU_001_001_001", "d_name": "Lobster", "about": "spicy", "price": "20", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "New Dish Added Successfully"},
    {"id": "TC_ADD_MENU_001_001_002", "d_name": "Lobster", "about": "Extra_spicy!", "price": "20", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "New Dish Added Successfully"},
    {"id": "TC_ADD_MENU_001_001_003", "d_name": "Lobster", "about": "1234567", "price": "20", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "New Dish Added Successfully"},
    {"id": "TC_ADD_MENU_001_001_004", "d_name": "Lobster", "about": "Extra Spicy", "price": "20", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "New Dish Added Successfully"},
    {"id": "TC_ADD_MENU_001_002_001", "d_name": "Lobster Thermidor", "about": "spicy", "price": "20", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "New Dish Added Successfully"},
    {"id": "TC_ADD_MENU_001_002_002", "d_name": "Lobster Thermidor", "about": "Extra_spicy!", "price": "20", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "New Dish Added Successfully"},
    {"id": "TC_ADD_MENU_001_002_003", "d_name": "Lobster Thermidor", "about": "1234567", "price": "20", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "New Dish Added Successfully"},
    {"id": "TC_ADD_MENU_001_002_004", "d_name": "Lobster Thermidor", "about": "Extra Spicy", "price": "20", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "New Dish Added Successfully"},
    {"id": "TC_ADD_MENU_001_003_001", "d_name": "Lobster-Thermidor", "about": "spicy", "price": "20", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "New Dish Added Successfully"},
    {"id": "TC_ADD_MENU_001_003_002", "d_name": "Lobster-Thermidor", "about": "Extra_spicy!", "price": "20", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "New Dish Added Successfully"},
    {"id": "TC_ADD_MENU_001_003_003", "d_name": "Lobster-Thermidor", "about": "1234567", "price": "20", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "New Dish Added Successfully"},
    {"id": "TC_ADD_MENU_001_003_004", "d_name": "Lobster-Thermidor", "about": "Extra Spicy", "price": "20", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "New Dish Added Successfully"},
    {"id": "TC_ADD_MENU_002_001_001", "d_name": "!@#$%^&*", "about": "spicy", "price": "20", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Unsuccessful add menu to list"},
    {"id": "TC_ADD_MENU_002_001_002", "d_name": "!@#$%^&*", "about": "Extra_spicy!", "price": "20", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Unsuccessful add menu to list"},
    {"id": "TC_ADD_MENU_002_001_003", "d_name": "!@#$%^&*", "about": "1234567", "price": "20", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Unsuccessful add menu to list"},
    {"id": "TC_ADD_MENU_002_001_004", "d_name": "!@#$%^&*", "about": "Extra Spicy", "price": "20", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Unsuccessful add menu to list"},
    {"id": "TC_ADD_MENU_002_002_001", "d_name": "1234567", "about": "spicy", "price": "20", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Unsuccessful add menu to list"},
    {"id": "TC_ADD_MENU_002_002_002", "d_name": "1234567", "about": "Extra_spicy!", "price": "20", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Unsuccessful add menu to list"},
    {"id": "TC_ADD_MENU_002_002_003", "d_name": "1234567", "about": "1234567", "price": "20", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Unsuccessful add menu to list"},
    {"id": "TC_ADD_MENU_002_002_004", "d_name": "1234567", "about": "Extra Spicy", "price": "20", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Unsuccessful add menu to list"},
    {"id": "TC_ADD_MENU_002_003_001", "d_name": "   ", "about": "spicy", "price": "20", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Unsuccessful add menu to list"},
    {"id": "TC_ADD_MENU_002_003_002", "d_name": "   ", "about": "Extra_spicy!", "price": "20", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Unsuccessful add menu to list"},
    {"id": "TC_ADD_MENU_002_003_003", "d_name": "   ", "about": "1234567", "price": "20", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Unsuccessful add menu to list"},
    {"id": "TC_ADD_MENU_002_003_004", "d_name": "   ", "about": "Extra Spicy", "price": "20", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Unsuccessful add menu to list"},
    {"id": "TC_ADD_MENU_003_001_001", "d_name": "Lobster", "about": "!@#$%^&*", "price": "20", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Unsuccessful add menu to list"},
    {"id": "TC_ADD_MENU_003_001_002", "d_name": "Lobster Thermidor", "about": "!@#$%^&*", "price": "20", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Unsuccessful add menu to list"},
    {"id": "TC_ADD_MENU_003_001_003", "d_name": "Lobster-Thermidor", "about": "!@#$%^&*", "price": "20", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Unsuccessful add menu to list"},
    {"id": "TC_ADD_MENU_004_001_001", "d_name": "Lobster", "about": "spicy", "price": "Alif", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Unsuccessful add menu to list"},
    {"id": "TC_ADD_MENU_004_001_002", "d_name": "Lobster Thermidor", "about": "spicy", "price": "@abc123", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Unsuccessful add menu to list"},
    {"id": "TC_ADD_MENU_004_001_003", "d_name": "Lobster-Thermidor", "about": "spicy", "price": "!@#$%^&*", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Unsuccessful add menu to list"},
    {"id": "TC_ADD_MENU_004_001_004", "d_name": "Lobster-Thermidor", "about": "spicy", "price": "2  0", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Unsuccessful add menu to list"},
    {"id": "TC_ADD_MENU_004_001_005", "d_name": "Lobster-Thermidor", "about": "spicy", "price": "   ", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Unsuccessful add menu to list"},
    {"id": "TC_ADD_MENU_004_002_001", "d_name": "Lobster", "about": "Extra_spicy!", "price": "Alif", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Unsuccessful add menu to list"},
    {"id": "TC_ADD_MENU_004_002_002", "d_name": "Lobster Thermidor", "about": "Extra_spicy!", "price": "@abc123", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Unsuccessful add menu to list"},
    {"id": "TC_ADD_MENU_004_002_003", "d_name": "Lobster-Thermidor", "about": "Extra_spicy!", "price": "!@#$%^&*", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Unsuccessful add menu to list"},
    {"id": "TC_ADD_MENU_004_002_004", "d_name": "Lobster-Thermidor", "about": "Extra_spicy!", "price": "2  0", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Unsuccessful add menu to list"},
    {"id": "TC_ADD_MENU_004_002_005", "d_name": "Lobster-Thermidor", "about": "Extra_spicy!", "price": "   ", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Unsuccessful add menu to list"},
    {"id": "TC_ADD_MENU_004_003_001", "d_name": "Lobster", "about": "1234567", "price": "Alif", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Unsuccessful add menu to list"},
    {"id": "TC_ADD_MENU_004_003_002", "d_name": "Lobster Thermidor", "about": "1234567", "price": "@abc123", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Unsuccessful add menu to list"},
    {"id": "TC_ADD_MENU_004_003_003", "d_name": "Lobster-Thermidor", "about": "1234567", "price": "!@#$%^&*", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Unsuccessful add menu to list"},
    {"id": "TC_ADD_MENU_004_003_004", "d_name": "Lobster-Thermidor", "about": "1234567", "price": "2  0", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Unsuccessful add menu to list"},
    {"id": "TC_ADD_MENU_004_003_005", "d_name": "Lobster-Thermidor", "about": "1234567", "price": "   ", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Unsuccessful add menu to list"},
    {"id": "TC_ADD_MENU_004_004_001", "d_name": "Lobster", "about": "Extra spicy", "price": "Alif", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Unsuccessful add menu to list"},
    {"id": "TC_ADD_MENU_004_004_002", "d_name": "Lobster Thermidor", "about": "Extra spicy", "price": "@abc123", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Unsuccessful add menu to list"},
    {"id": "TC_ADD_MENU_004_004_003", "d_name": "Lobster-Thermidor", "about": "Extra spicy", "price": "!@#$%^&*", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Unsuccessful add menu to list"},
    {"id": "TC_ADD_MENU_004_004_004", "d_name": "Lobster-Thermidor", "about": "Extra spicy", "price": "2  0", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Unsuccessful add menu to list"},
    {"id": "TC_ADD_MENU_004_004_005", "d_name": "Lobster-Thermidor", "about": "Extra spicy", "price": "   ", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Unsuccessful add menu to list"},
    {"id": "TC_ADD_MENU_004_005_001", "d_name": "!@#$%^&*", "about": "!@#$%^&*", "price": "Alif", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Unsuccessful add menu to list"},
    {"id": "TC_ADD_MENU_004_005_002", "d_name": "!@#$%^&*", "about": "!@#$%^&*", "price": "@abc123", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Unsuccessful add menu to list"},
    {"id": "TC_ADD_MENU_004_005_003", "d_name": "!@#$%^&*", "about": "!@#$%^&*", "price": "!@#$%^&*", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Unsuccessful add menu to list"},
    {"id": "TC_ADD_MENU_004_005_004", "d_name": "!@#$%^&*", "about": "!@#$%^&*", "price": "3  2", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Unsuccessful add menu to list"},
    {"id": "TC_ADD_MENU_004_005_005", "d_name": "!@#$%^&*", "about": "!@#$%^&*", "price": "   ", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Unsuccessful add menu to list"},
    {"id": "TC_ADD_MENU_004_006_001", "d_name": "1234567", "about": "!@#$%^&*", "price": "Alif", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Unsuccessful add menu to list"},
    {"id": "TC_ADD_MENU_004_006_002", "d_name": "1234567", "about": "!@#$%^&*", "price": "@abc123", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Unsuccessful add menu to list"},
    {"id": "TC_ADD_MENU_004_006_003", "d_name": "1234567", "about": "!@#$%^&*", "price": "!@#$%^&*", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Unsuccessful add menu to list"},
    {"id": "TC_ADD_MENU_004_006_004", "d_name": "1234567", "about": "!@#$%^&*", "price": "3  2", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Unsuccessful add menu to list"},
    {"id": "TC_ADD_MENU_004_006_005", "d_name": "1234567", "about": "!@#$%^&*", "price": "   ", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Unsuccessful add menu to list"},
    # Add other test cases here...
]

# Iterate over test cases
for test_case in test_cases:
    # Open the add menu page
    driver.get(url)
    # Wait for the page to load
    time.sleep(3)

    # Fill the form with test data
    driver.find_element(By.NAME, "d_name").clear()
    driver.find_element(By.NAME, "d_name").send_keys(test_case["d_name"])

    driver.find_element(By.NAME, "about").clear()
    driver.find_element(By.NAME, "about").send_keys(test_case["about"])

    driver.find_element(By.NAME, "price").clear()
    driver.find_element(By.NAME, "price").send_keys(test_case["price"])

    driver.find_element(By.NAME, "file").send_keys(test_case["image"])

    # Select restaurant (assuming there is always at least one restaurant in the dropdown)
    select_restaurant = driver.find_element(By.NAME, "res_name")
    select_restaurant.find_elements(By.TAG_NAME, "option")[1].click()  # Select the second option (first option is the placeholder)

    # Click the "Save" button
    driver.find_element(By.CSS_SELECTOR, "input[type='submit'][value='Save']").click()

    # Wait for the result message to appear
    try:
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'alert')]"))
        )
        if test_case["expected_result"] in success_message.text:
            print(f"Test case {test_case['id']}: PASS")
        else:
            print(f"Test case {test_case['id']}: FAIL - Unexpected success message")
    except Exception as e:
        print(f"Test case {test_case['id']}: FAIL - Error: {str(e)}")

# Close the driver
driver.quit()
