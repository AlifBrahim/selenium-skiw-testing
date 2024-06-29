import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Function to log in (assuming login is required before editing a menu)
def login():
    driver.get("http://localhost/Online-Food-Ordering-System-in-PHP/admin/index.php")
    time.sleep(3)
    driver.find_element(By.NAME, "username").send_keys("admin")
    driver.find_element(By.NAME, "password").send_keys("1234567")
    driver.find_element(By.NAME, "submit").click()
    time.sleep(3)

# Log in first
login()

# URL of the edit menu page
url = "http://localhost/Online-Food-Ordering-System-in-PHP/admin/update_menu.php?menu_upd=105"

# Define test data for editing a menu
test_cases = [
    {"id": "TC_ADD_MENU_001_001_001", "d_name": "Lobster", "about": "spicy", "price": "20", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_001_001_002", "d_name": "Lobster", "about": "Extra_spicy!", "price": "20", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_001_001_003", "d_name": "Lobster", "about": "1234567", "price": "20", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_001_001_004", "d_name": "Lobster", "about": "Extra Spicy", "price": "20", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_001_002_001", "d_name": "Lobster Thermidor", "about": "spicy", "price": "20", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_001_002_002", "d_name": "Lobster Thermidor", "about": "Extra_spicy!", "price": "20", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_001_002_003", "d_name": "Lobster Thermidor", "about": "1234567", "price": "20", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_001_002_004", "d_name": "Lobster Thermidor", "about": "Extra Spicy", "price": "20", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_001_003_001", "d_name": "Lobster-Thermidor", "about": "spicy", "price": "20", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_001_003_002", "d_name": "Lobster-Thermidor", "about": "Extra_spicy!", "price": "20", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_001_003_003", "d_name": "Lobster-Thermidor", "about": "1234567", "price": "20", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_001_003_004", "d_name": "Lobster-Thermidor", "about": "Extra Spicy", "price": "20", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_002_001_001", "d_name": "!@#$%^&*", "about": "spicy", "price": "20", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_002_001_002", "d_name": "!@#$%^&*", "about": "Extra_spicy!", "price": "20", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_002_001_003", "d_name": "!@#$%^&*", "about": "1234567", "price": "20", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_002_001_004", "d_name": "!@#$%^&*", "about": "Extra Spicy", "price": "20", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_002_002_001", "d_name": "1234567", "about": "spicy", "price": "20", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_002_002_002", "d_name": "1234567", "about": "Extra_spicy!", "price": "20", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_002_002_003", "d_name": "1234567", "about": "1234567", "price": "20", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_002_002_004", "d_name": "1234567", "about": "Extra Spicy", "price": "20", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_002_003_001", "d_name": "   ", "about": "spicy", "price": "20", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_002_003_002", "d_name": "   ", "about": "Extra_spicy!", "price": "20", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_002_003_003", "d_name": "   ", "about": "1234567", "price": "20", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_002_003_004", "d_name": "   ", "about": "Extra Spicy", "price": "20", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_003_001_001", "d_name": "Lobster", "about": "!@#$%^&*", "price": "20", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_003_001_002", "d_name": "Lobster Thermidor", "about": "!@#$%^&*", "price": "20", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_003_001_003", "d_name": "Lobster-Thermidor", "about": "!@#$%^&*", "price": "20", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_004_001_001", "d_name": "Lobster", "about": "spicy", "price": "Alif", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_004_001_002", "d_name": "Lobster Thermidor", "about": "spicy", "price": "@abc123", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_004_001_003", "d_name": "Lobster-Thermidor", "about": "spicy", "price": "!@#$%^&*", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_004_001_004", "d_name": "Lobster-Thermidor", "about": "spicy", "price": "2  0", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_004_001_005", "d_name": "Lobster-Thermidor", "about": "spicy", "price": "   ", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_004_002_001", "d_name": "Lobster", "about": "Extra_spicy!", "price": "Alif", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_004_002_002", "d_name": "Lobster Thermidor", "about": "Extra_spicy!", "price": "@abc123", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_004_002_003", "d_name": "Lobster-Thermidor", "about": "Extra_spicy!", "price": "!@#$%^&*", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_004_002_004", "d_name": "Lobster-Thermidor", "about": "Extra_spicy!", "price": "2  0", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_004_002_005", "d_name": "Lobster-Thermidor", "about": "Extra_spicy!", "price": "   ", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_004_003_001", "d_name": "Lobster", "about": "1234567", "price": "Alif", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_004_003_002", "d_name": "Lobster Thermidor", "about": "1234567", "price": "@abc123", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_004_003_003", "d_name": "Lobster-Thermidor", "about": "1234567", "price": "!@#$%^&*", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_004_003_004", "d_name": "Lobster-Thermidor", "about": "1234567", "price": "2  0", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_004_003_005", "d_name": "Lobster-Thermidor", "about": "1234567", "price": "   ", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_004_004_001", "d_name": "Lobster", "about": "Extra spicy", "price": "Alif", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_004_004_002", "d_name": "Lobster Thermidor", "about": "Extra spicy", "price": "@abc123", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_004_004_003", "d_name": "Lobster-Thermidor", "about": "Extra spicy", "price": "!@#$%^&*", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_004_004_004", "d_name": "Lobster-Thermidor", "about": "Extra spicy", "price": "2  0", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_004_004_005", "d_name": "Lobster-Thermidor", "about": "Extra spicy", "price": "   ", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_004_005_001", "d_name": "!@#$%^&*", "about": "!@#$%^&*", "price": "Alif", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_004_005_002", "d_name": "!@#$%^&*", "about": "!@#$%^&*", "price": "@abc123", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_004_005_003", "d_name": "!@#$%^&*", "about": "!@#$%^&*", "price": "!@#$%^&*", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_004_005_004", "d_name": "!@#$%^&*", "about": "!@#$%^&*", "price": "3  2", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_004_005_005", "d_name": "!@#$%^&*", "about": "!@#$%^&*", "price": "   ", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_004_006_001", "d_name": "1234567", "about": "!@#$%^&*", "price": "Alif", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_004_006_002", "d_name": "1234567", "about": "!@#$%^&*", "price": "@abc123", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_004_006_003", "d_name": "1234567", "about": "!@#$%^&*", "price": "!@#$%^&*", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_004_006_004", "d_name": "1234567", "about": "!@#$%^&*", "price": "3  2", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_004_006_005", "d_name": "1234567", "about": "!@#$%^&*", "price": "   ", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_004_007_001", "d_name": "   ", "about": "!@#$%^&*", "price": "Alif", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_004_007_002", "d_name": "   ", "about": "!@#$%^&*", "price": "@abc123", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_004_007_003", "d_name": "   ", "about": "!@#$%^&*", "price": "!@#$%^&*", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_004_007_004", "d_name": "   ", "about": "!@#$%^&*", "price": "3  2", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_004_007_005", "d_name": "   ", "about": "!@#$%^&*", "price": "   ", "image": "C:/Users/User/Downloads/spaghetti.jpg", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_004_008_001", "d_name": "!@#$%^&*", "about": "!@#$%^&*", "price": "Alif", "image": "C:/Users/User/Downloads/QUIS.pdf", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_004_008_002", "d_name": "!@#$%^&*", "about": "!@#$%^&*", "price": "@abc123", "image": "C:/Users/User/Downloads/QUIS.pdf", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_004_008_003", "d_name": "!@#$%^&*", "about": "!@#$%^&*", "price": "!@#$%^&*", "image": "C:/Users/User/Downloads/QUIS.pdf", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_004_008_004", "d_name": "!@#$%^&*", "about": "!@#$%^&*", "price": "3  2", "image": "C:/Users/User/Downloads/QUIS.pdf", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_004_008_005", "d_name": "!@#$%^&*", "about": "!@#$%^&*", "price": "   ", "image": "C:/Users/User/Downloads/QUIS.pdf", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_004_009_001", "d_name": "1234567", "about": "!@#$%^&*", "price": "Alif", "image": "C:/Users/User/Downloads/QUIS.pdf", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_004_009_002", "d_name": "1234567", "about": "!@#$%^&*", "price": "@abc123", "image": "C:/Users/User/Downloads/QUIS.pdf", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_004_009_003", "d_name": "1234567", "about": "!@#$%^&*", "price": "!@#$%^&*", "image": "C:/Users/User/Downloads/QUIS.pdf", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_004_009_004", "d_name": "1234567", "about": "!@#$%^&*", "price": "3  2", "image": "C:/Users/User/Downloads/QUIS.pdf", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_004_009_005", "d_name": "1234567", "about": "!@#$%^&*", "price": "   ", "image": "C:/Users/User/Downloads/QUIS.pdf", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_004_010_001", "d_name": "   ", "about": "!@#$%^&*", "price": "Alif", "image": "C:/Users/User/Downloads/QUIS.pdf", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_004_010_002", "d_name": "   ", "about": "!@#$%^&*", "price": "@abc123", "image": "C:/Users/User/Downloads/QUIS.pdf", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_004_010_003", "d_name": "   ", "about": "!@#$%^&*", "price": "!@#$%^&*", "image": "C:/Users/User/Downloads/QUIS.pdf", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_004_010_004", "d_name": "   ", "about": "!@#$%^&*", "price": "3  2", "image": "C:/Users/User/Downloads/QUIS.pdf", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_004_010_005", "d_name": "   ", "about": "!@#$%^&*", "price": "   ", "image": "C:/Users/User/Downloads/QUIS.pdf", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_004_011_001", "d_name": "!@#$%^&*", "about": "!@#$%^&*", "price": "Alif", "image": "", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_004_011_002", "d_name": "!@#$%^&*", "about": "!@#$%^&*", "price": "@abc123", "image": "", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_004_011_003", "d_name": "!@#$%^&*", "about": "!@#$%^&*", "price": "!@#$%^&*", "image": "", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_004_011_004", "d_name": "!@#$%^&*", "about": "!@#$%^&*", "price": "3  2", "image": "", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_004_011_005", "d_name": "!@#$%^&*", "about": "!@#$%^&*", "price": "   ", "image": "", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_004_012_001", "d_name": "1234567", "about": "!@#$%^&*", "price": "Alif", "image": "", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_004_012_002", "d_name": "1234567", "about": "!@#$%^&*", "price": "@abc123", "image": "", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_004_012_003", "d_name": "1234567", "about": "!@#$%^&*", "price": "!@#$%^&*", "image": "", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_004_012_004", "d_name": "1234567", "about": "!@#$%^&*", "price": "3  2", "image": "", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_004_012_005", "d_name": "1234567", "about": "!@#$%^&*", "price": "   ", "image": "", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_004_013_001", "d_name": "   ", "about": "!@#$%^&*", "price": "Alif", "image": "", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_004_013_002", "d_name": "   ", "about": "!@#$%^&*", "price": "@abc123", "image": "", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_004_013_003", "d_name": "   ", "about": "!@#$%^&*", "price": "!@#$%^&*", "image": "", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_004_013_004", "d_name": "   ", "about": "!@#$%^&*", "price": "3  2", "image": "", "expected_result": "Record Updated!"},
    {"id": "TC_ADD_MENU_004_013_005", "d_name": "   ", "about": "!@#$%^&*", "price": "   ", "image": "", "expected_result": "Record Updated!"}
]
# Function to check if file exists and return correct path
def get_file_path(file_name):
    base_path = "C:/Users/User/Downloads/"
    full_path = os.path.join(base_path, file_name)
    if os.path.exists(full_path):
        return full_path
    else:
        return None

# Iterate over test cases
for test_case in test_cases:
    # Open the edit menu page
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

    image_path = get_file_path(os.path.basename(test_case["image"]))
    if image_path:
        driver.find_element(By.NAME, "file").send_keys(image_path)
    else:
        print(f"Test case {test_case['id']}: FAIL - Image file not found: {test_case['image']}")
        continue

    # Select restaurant (assuming there is always at least one restaurant in the dropdown)
    select_restaurant = driver.find_element(By.NAME, "res_name")
    select_restaurant.find_elements(By.TAG_NAME, "option")[1].click()  # Select the second option (first option is the placeholder)

    # Click the "Save" button
    driver.find_element(By.NAME, "submit").click()
    time.sleep(3)

    # Check the result
    try:
        message = driver.find_element(By.CLASS_NAME, "alert").text
        if test_case["expected_result"] in message:
            print(f"Test case {test_case['id']}: PASS")
        else:
            print(f"Test case {test_case['id']}: FAIL - Unexpected message: {message}")
    except Exception as e:
        error_message = str(e).split("\n")[0]
        print(f"Test case {test_case['id']}: FAIL - Error: {error_message}")

# Close the browser
driver.quit()