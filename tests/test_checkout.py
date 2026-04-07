import allure
import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.test_data import CheckoutInfo


@pytest.fixture
def checkout_driver(logged_in_driver):
    # Starts at checkout page — used by all checkout tests
    inventory = InventoryPage(logged_in_driver)
    inventory.add_backpack()
    inventory.go_to_cart()

    cart = CartPage(logged_in_driver)
    cart.click_checkout()
    return logged_in_driver


@allure.feature("Checkout")
class TestCheckout:

    @pytest.mark.smoke
    @allure.title("Checkout page loads correctly")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_checkout_page_loads(self, checkout_driver):
        checkout = CheckoutPage(checkout_driver)
        assert checkout.is_loaded()
        assert checkout.get_title() == "Checkout: Your Information"

    @pytest.mark.smoke
    @allure.title("Valid form submission proceeds to overview")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_valid_form_proceeds(self, checkout_driver):
        checkout = CheckoutPage(checkout_driver)
        checkout.fill_form(**CheckoutInfo.VALID)
        checkout.click_continue()
        assert "checkout-step-two" in checkout_driver.current_url

    @pytest.mark.regression
    @allure.title("Form fails with missing first name")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_missing_first_name(self, checkout_driver):
        checkout = CheckoutPage(checkout_driver)
        checkout.fill_form(**CheckoutInfo.MISSING_FIRST)
        checkout.click_continue()
        assert "First Name is required" in checkout.get_error_message()

    @pytest.mark.regression
    @allure.title("Form fails with missing last name")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_missing_last_name(self, checkout_driver):
        checkout = CheckoutPage(checkout_driver)
        checkout.fill_form(**CheckoutInfo.MISSING_LAST)
        checkout.click_continue()
        assert "Last Name is required" in checkout.get_error_message()

    @pytest.mark.regression
    @allure.title("Form fails with missing postal code")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_missing_postal_code(self, checkout_driver):
        checkout = CheckoutPage(checkout_driver)
        checkout.fill_form(**CheckoutInfo.MISSING_ZIP)
        checkout.click_continue()
        assert "Postal Code is required" in checkout.get_error_message()

    @pytest.mark.regression
    @allure.title("Cancel button redirects back to cart")
    @allure.severity(allure.severity_level.NORMAL)
    def test_cancel_redirects_to_cart(self, checkout_driver):
        checkout = CheckoutPage(checkout_driver)
        checkout.click_cancel()
        assert "cart" in checkout_driver.current_url
