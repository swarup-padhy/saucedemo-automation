import allure
import pytest
from pages.inventory_page import InventoryPage


@allure.feature("Inventory")
class TestInventory:
    @pytest.mark.smoke
    @allure.title("Inventory page loads after login")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_inventory_page_loads(self, logged_in_driver):
        inventory = InventoryPage(logged_in_driver)
        assert inventory.is_loaded()
        assert inventory.get_title() == "Products"

    ...

    @pytest.mark.smoke
    @allure.title("Add single item to cart")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_one_item_to_cart(self, logged_in_driver):
        inventory = InventoryPage(logged_in_driver)
        inventory.add_backpack()
        assert inventory.get_cart_count() == "1"

    ...

    @pytest.mark.regression
    @allure.title("Add multiple items to cart")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_multiple_items_to_cart(self, logged_in_driver):
        inventory = InventoryPage(logged_in_driver)
        inventory.add_bolt_shirt()
        inventory.add_onesie()
        assert inventory.get_cart_count() == "2"
