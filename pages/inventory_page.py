from selenium.webdriver.common.by import By


class InventoryPage:
    # --- Locators ---
    TITLE           = (By.CLASS_NAME, "title")
    CART_ICON       = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE      = (By.CLASS_NAME, "shopping_cart_badge")

    # Add to cart buttons — by product name
    ADD_BOLT_SHIRT  = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ADD_ONESIE      = (By.ID, "add-to-cart-sauce-labs-onesie")
    ADD_BACKPACK    = (By.ID, "add-to-cart-sauce-labs-backpack")
    ADD_BIKE_LIGHT  = (By.ID, "add-to-cart-sauce-labs-bike-light")
    ADD_FLEECE      = (By.ID, "add-to-cart-sauce-labs-fleece-jacket")
    ADD_RED_SHIRT   = (By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")

    def __init__(self, driver):
        self.driver = driver

    # --- Actions ---
    def is_loaded(self):
        return "inventory" in self.driver.current_url

    def get_title(self):
        return self.driver.find_element(*self.TITLE).text

    def add_bolt_shirt(self):
        self.driver.find_element(*self.ADD_BOLT_SHIRT).click()

    def add_onesie(self):
        self.driver.find_element(*self.ADD_ONESIE).click()

    def add_backpack(self):
        self.driver.find_element(*self.ADD_BACKPACK).click()

    def go_to_cart(self):
        self.driver.find_element(*self.CART_ICON).click()

    def get_cart_count(self):
        return self.driver.find_element(*self.CART_BADGE).text
