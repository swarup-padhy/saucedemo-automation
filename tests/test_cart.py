import allure
import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


@allure.feature("Cart")
class TestCart:

    @pytest.mark.smoke
    @allure.title("Cart page loads with added items")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_cart_loads_with_items(self, logged_in_driver):
        inventory = InventoryPage(logged_in_driver)
        inventory.add_bolt_shirt()
        inventory.add_onesie()
        inventory.go_to_cart()

        cart = CartPage(logged_in_driver)
        assert cart.is_loaded()
        assert cart.get_item_count() == 2

    @pytest.mark.regression
    @allure.title("Remove item from cart")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_remove_item_from_cart(self, logged_in_driver):
        inventory = InventoryPage(logged_in_driver)
        inventory.add_bolt_shirt()
        inventory.add_onesie()
        inventory.go_to_cart()

        cart = CartPage(logged_in_driver)
        cart.remove_bolt_shirt()
        assert cart.get_item_count() == 1

    @pytest.mark.regression
    @allure.title("Continue shopping redirects to inventory")
    @allure.severity(allure.severity_level.NORMAL)
    def test_continue_shopping(self, logged_in_driver):
        inventory = InventoryPage(logged_in_driver)
        inventory.add_backpack()
        inventory.go_to_cart()

        cart = CartPage(logged_in_driver)
        cart.click_continue_shopping()
        assert "inventory" in logged_in_driver.current_url

    @pytest.mark.regression
    @allure.title("Checkout button redirects to checkout page")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_checkout_button_redirects(self, logged_in_driver):
        inventory = InventoryPage(logged_in_driver)
        inventory.add_backpack()
        inventory.go_to_cart()

        cart = CartPage(logged_in_driver)
        cart.click_checkout()
        assert "checkout-step-one" in logged_in_driver.current_url
