import os
import pytest
from src.utils.helper_function import update_default_browser, update_headless_mode

def main(test_files):

    # Allure report
    args = ["-v", "-s", "--alluredir=./reports/allure-results"]  # Specify Allure results directory
    pytest.main(args + test_files)

    generate_allure_report()

def generate_allure_report():
    print("Generating Allure report...")
    result = os.system("allure generate ./reports/allure-results -o ./reports/allure-report --clean")
    if result != 0:
        print("Failed to generate Allure report.")
    else:
        print("Allure report generated successfully.")

    

if __name__ == "__main__":
    # Choose browser from "chrome" or "firefox"
    browser = "chrome"

    # Define headless mode - True or False
    headless = True

    # Update default browser setting
    update_default_browser(browser)

    # Update headless mode setting
    update_headless_mode(headless)
 
    test_files = [
        "src/tests/login/test_login.py",
    ]

    # Run tests
    main(test_files)
