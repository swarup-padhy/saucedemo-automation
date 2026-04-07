from dbm import error

import allure
import pytest
from conftest import driver
from pages.login_page import LoginPage
from utils.test_data import Users


@allure.feature("Authentication")
class TestLogin:

    @pytest.mark.smoke
    @allure.title("Valid login redirects to inventory page")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_valid_login(self, driver):
        login = LoginPage(driver)
        login.open()
        login.login("standard_user", "secret_sauce")
        assert "inventory" in driver.current_url

    ...

    @pytest.mark.regression
    @allure.title("Login fails with wrong password")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_invalid_password(self, driver):
        login = LoginPage(driver)
        login.open()
        login.login("standard_user", "wrong_password")
        error = login.get_error_message()
        assert "Username and password do not match" in error

    ...

    @pytest.mark.regression
    @allure.title("Login fails with empty username")
    @allure.severity(allure.severity_level.NORMAL)
    def test_empty_username(self, driver):
        login = LoginPage(driver)
        login.open()
        login.login("", "secret_sauce")
        error = login.get_error_message()
        assert "Username is required" in error

    ...

    @pytest.mark.regression
    @allure.title("Login fails with empty password")
    @allure.severity(allure.severity_level.NORMAL)
    def test_empty_password(self, driver):
        login = LoginPage(driver)
        login.open()
        login.login("standard_user", "")
        error = login.get_error_message()
        assert "Password is required" in error

    ...

    @pytest.mark.smoke
    @allure.title("Locked out user cannot login")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_locked_out_user(self, driver):
        login = LoginPage(driver)
        login.open()
        login.login(
            Users.LOCKED["username"],
            Users.LOCKED["password"]
        )
        error = login.get_error_message()
        assert "locked out" in error
