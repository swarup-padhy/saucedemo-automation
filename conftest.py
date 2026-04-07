import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from utils.test_data import Users


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    })

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)

    yield driver

    driver.quit()


@pytest.fixture(scope="function")
def logged_in_driver(driver):
    # Logs in once — hands ready-logged-in driver to any test that needs it
    login = LoginPage(driver)
    login.open()
    login.login(Users.STANDARD["username"], Users.STANDARD["password"])
    return driver
