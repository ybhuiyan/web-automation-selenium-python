import os
import pytest
from src.utils.helper_function import update_default_browser, update_headless_mode
import subprocess

def main(test_files):
    # Define pytest arguments for generating Allure results
    args = ["-v", "-s", "--alluredir=./reports/allure-results"]
    pytest.main(args + test_files)

    # Generate Allure report after tests
    generate_allure_report()

def generate_allure_report():
    print("Generating Allure report...")
    try:
        # Using subprocess to run the Allure generation command
        result = subprocess.run(
            ["allure", "generate", "./reports/allure-results", "-o", "./reports/allure-report", "--clean"],
            check=True,
            capture_output=True,
            text=True
        )
        print("Allure report generated successfully at './reports/allure-report'.")
    except subprocess.CalledProcessError as e:
        print("Failed to generate Allure report.")
        print(e.output)

if __name__ == "__main__":
    # Set browser and headless mode configuration
    browser = "chrome"
    headless = True

    # Apply configuration
    update_default_browser(browser)
    update_headless_mode(headless)

    # List of test files to run
    test_files = [
        "src/tests/login/test_login.py",
    ]

    # Run tests and generate the report
    main(test_files)
