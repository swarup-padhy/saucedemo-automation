import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from utils.test_data import Users, Config


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    })

    # --- Headless mode ---
    if Config.HEADLESS:
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)

    yield driver

    driver.quit()


@pytest.fixture(scope="function")
def logged_in_driver(driver):
    login = LoginPage(driver)
    login.open()
    login.login(Users.STANDARD["username"], Users.STANDARD["password"])
    return driver


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver") or item.funcargs.get("logged_in_driver")

        if driver:
            test_name = item.name.replace(" ", "_")
            screenshot_path = f"screenshots/{test_name}.png"
            driver.save_screenshot(screenshot_path)

            with open(screenshot_path, "rb") as f:
                allure.attach(
                    f.read(),
                    name=f"FAILED — {test_name}",
                    attachment_type=allure.attachment_type.PNG
                )
