from selenium import webdriver
import time

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Define test data
test_cases = [
    {"id": "TC_SIGN_UP_001", "username": "alifibrahizmm1", "firstname": "Muhammad", "lastname": "Alif", "email": "alif2341@gmail.com", "phone": "1384728439", "password": "alif1234", "cpassword": "alif1234", "address": "No.11, Sisiran Sintok", "expected_result": "login.php"},
    {"id": "TC_SIGN_UP_002", "username": "&*(*^&^1", "firstname": "Muhammad", "lastname": "Alif", "email": "alif2111@gmail.com", "phone": "1384728439", "password": "alif1234", "cpassword": "alif1234", "address": "No.11, Sisiran Sintok", "expected_result": "registration.php"},
    {"id": "TC_SIGN_UP_003", "username": "alif ibrahim1", "firstname": "Muhammad", "lastname": "Alif", "email": "alif34551@gmail.com", "phone": "1384728439", "password": "alif1234", "cpassword": "alif1234", "address": "No.11, Sisiran Sintok", "expected_result": "registration.php"},
    {"id": "TC_SIGN_UP_004", "username": " 1", "firstname": "Muhammad", "lastname": "Alif", "email": "alif444441@gmail.com", "phone": "1384728440", "password": "alif1234", "cpassword": "alif1234", "address": "No.11, Sisiran Sintok", "expected_result": "registration.php"},
    {"id": "TC_SIGN_UP_005", "username": "alifibrahimas1", "firstname": "Mu7amad", "lastname": "Alif", "email": "alif554331@gmail.com", "phone": "1384728439", "password": "alif1234", "cpassword": "alif1234", "address": "No.11, Sisiran Sintok", "expected_result": "registration.php"},
    {"id": "TC_SIGN_UP_006", "username": "alifibrahixxmz1", "firstname": "&*(*^&^1", "lastname": "Alif", "email": "alif64321@gmail.com", "phone": "1384728440", "password": "alif1234", "cpassword": "alif1234", "address": "No.11, Sisiran Sintok", "expected_result": "registration.php"},
    {"id": "TC_SIGN_UP_007", "username": "alifibrahim1", "firstname": "123", "lastname": "Alif", "email": "alif65431@gmail.com", "phone": "1384728439", "password": "alif1234", "cpassword": "alif1234", "address": "No.11, Sisiran Sintok", "expected_result": "registration.php"},
    {"id": "TC_SIGN_UP_008", "username": "alifibrahim2", "firstname": " ", "lastname": "Alif", "email": "alif56431@gmail.com", "phone": "1384728441", "password": "alif1234", "cpassword": "alif1234", "address": "No.11, Sisiran Sintok", "expected_result": "registration.php"},
    {"id": "TC_SIGN_UP_009", "username": "alifibrahim3", "firstname": "Muhammad", "lastname": "abc123", "email": "alif77651@gmail.com", "phone": "1384728442", "password": "alif1234", "cpassword": "alif1234", "address": "No.11, Sisiran Sintok", "expected_result": "registration.php"},
    {"id": "TC_SIGN_UP_010", "username": "alifibrahim4", "firstname": "Muhammad", "lastname": "&^*(&&(*^(", "email": "alif98431@gmail.com", "phone": "1384728443", "password": "alif1234", "cpassword": "alif1234", "address": "No.11, Sisiran Sintok", "expected_result": "registration.php"},
    {"id": "TC_SIGN_UP_011", "username": "alifibrahim5", "firstname": "Muhammad", "lastname": "123", "email": "alif23431@gmail.com", "phone": "1384728444", "password": "alif1234", "cpassword": "alif1234", "address": "No.11, Sisiran Sintok", "expected_result": "registration.php"},
    {"id": "TC_SIGN_UP_012", "username": "alifibrahim6", "firstname": "Muhammad", "lastname": " ", "email": "alif43431@gmail.com", "phone": "1384728445", "password": "alif1234", "cpassword": "alif1234", "address": "No.11, Sisiran Sintok", "expected_result": "registration.php"},
    {"id": "TC_SIGN_UP_013", "username": "alifibrahim7", "firstname": "Muhammad", "lastname": "Alif", "email": "alif@gmail1", "phone": "1384728446", "password": "alif1234", "cpassword": "alif1234", "address": "No.11, Sisiran Sintok", "expected_result": "registration.php"},
    {"id": "TC_SIGN_UP_014", "username": "alifibrahim8", "firstname": "Muhammad", "lastname": "Alif", "email": "alifgmail.com1", "phone": "1384728447", "password": "alif1234", "cpassword": "alif1234", "address": "No.11, Sisiran Sintok", "expected_result": "registration.php"},
    {"id": "TC_SIGN_UP_015", "username": "alifibrahim9", "firstname": "Muhammad", "lastname": "Alif", "email": "alif @gmail.com1", "phone": "1384728448", "password": "alif1234", "cpassword": "alif1234", "address": "No.11, Sisiran Sintok", "expected_result": "registration.php"},
    {"id": "TC_SIGN_UP_016", "username": "alifibrahim10", "firstname": "Muhammad", "lastname": "Alif", "email": "1231", "phone": "1384728449", "password": "alif1234", "cpassword": "alif1234", "address": "No.11, Sisiran Sintok", "expected_result": "registration.php"},
    {"id": "TC_SIGN_UP_017", "username": "alifibrahim11", "firstname": "Muhammad", "lastname": "Alif", "email": "alif@gmail.com1", "phone": "abc1", "password": "alif1234", "cpassword": "alif1234", "address": "No.11, Sisiran Sintok", "expected_result": "registration.php"},
    {"id": "TC_SIGN_UP_018", "username": "alifibrahim12", "firstname": "Muhammad", "lastname": "Alif", "email": "alif@gmail.com2", "phone": "abc1231", "password": "alif1234", "cpassword": "alif1234", "address": "No.11, Sisiran Sintok", "expected_result": "registration.php"},
    {"id": "TC_SIGN_UP_019", "username": "alifibrahim13", "firstname": "Muhammad", "lastname": "Alif", "email": "alif@gmail.com3", "phone": "&^*(&&(*^(1", "password": "alif1234", "cpassword": "alif1234", "address": "No.11, Sisiran Sintok", "expected_result": "registration.php"},
    {"id": "TC_SIGN_UP_020", "username": "alifibrahim14", "firstname": "Muhammad", "lastname": "Alif", "email": "alif@gmail.com4", "phone": " 1", "password": "alif1234", "cpassword": "alif1234", "address": "No.11, Sisiran Sintok", "expected_result": "registration.php"},
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
        error_message = str(e).split("\n")[0]
        print(f"Test case {test_case['id']}: FAIL - Error: {error_message}")

# Close the driver
driver.quit()
