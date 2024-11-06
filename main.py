import pytest
from src.utils.helper_function import update_default_browser, update_headless_mode

def main(test_files):
    # Specify Pytest arguments for verbose output, showing print statements, and generating an HTML report
    args = ["-v", "-s", "--html=reports/test_report.html", "--self-contained-html"]
    pytest.main(args + test_files)

if __name__ == "__main__":
    # Choose browser from "chrome" or "firefox"
    browser = "chrome"

    # Define headless mode - True or False
    headless = False

    # Update default browser setting
    update_default_browser(browser)

    # Update headless mode setting
    update_headless_mode(headless)
 
    test_files = [
        "src/tests/login/test_login.py",
    ]

    # Run tests
    main(test_files)
