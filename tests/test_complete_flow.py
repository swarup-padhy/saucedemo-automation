import allure
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_complete_page import CheckoutCompletePage


@allure.feature("End to End Flow")
class TestCompleteFlow:

    @pytest.mark.smoke
    @allure.title("Complete purchase flow from login to confirmation")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_complete_purchase(self, driver):
        # Step 1 — Login
        login = LoginPage(driver)
        login.open()
        login.login("standard_user", "secret_sauce")

        # Step 2 — Add item to cart
        inventory = InventoryPage(driver)
        assert inventory.is_loaded()
        inventory.add_backpack()
        assert inventory.get_cart_count() == "1"
        inventory.go_to_cart()

        # Step 3 — Verify cart and proceed
        cart = CartPage(driver)
        assert cart.is_loaded()
        assert cart.get_item_count() == 1
        cart.click_checkout()

        # Step 4 — Fill checkout form
        checkout = CheckoutPage(driver)
        assert checkout.is_loaded()
        checkout.fill_form("John", "Doe", "12345")
        checkout.click_continue()

        # Step 5 — Verify overview and finish
        overview = CheckoutOverviewPage(driver)
        assert overview.is_loaded()
        assert overview.get_title() == "Checkout: Overview"
        overview.click_finish()

        # Step 6 — Confirm order complete
        complete = CheckoutCompletePage(driver)
        assert complete.is_loaded()
        assert "Thank you" in complete.get_confirmation_message()
        assert complete.get_title() == "Checkout: Complete!"

    @pytest.mark.regression
    @allure.title("Cancel from overview redirects to inventory")
    @allure.severity(allure.severity_level.NORMAL)
    def test_cancel_from_overview(self, driver):
        login = LoginPage(driver)
        login.open()
        login.login("standard_user", "secret_sauce")

        inventory = InventoryPage(driver)
        inventory.add_backpack()
        inventory.go_to_cart()

        cart = CartPage(driver)
        cart.click_checkout()

        checkout = CheckoutPage(driver)
        checkout.fill_form("John", "Doe", "12345")
        checkout.click_continue()

        overview = CheckoutOverviewPage(driver)
        overview.click_cancel()

        assert "inventory" in driver.current_url

    @pytest.mark.regression
    @allure.title("Back home button returns to inventory after order")
    @allure.severity(allure.severity_level.NORMAL)
    def test_back_home_after_order(self, driver):
        login = LoginPage(driver)
        login.open()
        login.login("standard_user", "secret_sauce")

        inventory = InventoryPage(driver)
        inventory.add_backpack()
        inventory.go_to_cart()

        cart = CartPage(driver)
        cart.click_checkout()

        checkout = CheckoutPage(driver)
        checkout.fill_form("John", "Doe", "12345")
        checkout.click_continue()

        overview = CheckoutOverviewPage(driver)
        overview.click_finish()

        complete = CheckoutCompletePage(driver)
        assert complete.is_loaded()
        complete.click_back_home()

        assert "inventory" in driver.current_url
