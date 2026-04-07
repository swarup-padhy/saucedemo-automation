from selenium.webdriver.common.by import By


class CartPage:
    # --- Locators ---
    TITLE               = (By.CLASS_NAME, "title")
    CART_ITEMS          = (By.CLASS_NAME, "cart_item")
    REMOVE_BOLT_SHIRT   = (By.ID, "remove-sauce-labs-bolt-t-shirt")
    REMOVE_ONESIE       = (By.ID, "remove-sauce-labs-onesie")
    REMOVE_BACKPACK     = (By.ID, "remove-sauce-labs-backpack")
    CONTINUE_SHOPPING   = (By.ID, "continue-shopping")
    CHECKOUT_BUTTON     = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver

    # --- Actions ---
    def is_loaded(self):
        return "cart" in self.driver.current_url

    def get_title(self):
        return self.driver.find_element(*self.TITLE).text

    def get_item_count(self):
        return len(self.driver.find_elements(*self.CART_ITEMS))

    def remove_bolt_shirt(self):
        self.driver.find_element(*self.REMOVE_BOLT_SHIRT).click()

    def remove_onesie(self):
        self.driver.find_element(*self.REMOVE_ONESIE).click()

    def remove_backpack(self):
        self.driver.find_element(*self.REMOVE_BACKPACK).click()

    def click_continue_shopping(self):
        self.driver.find_element(*self.CONTINUE_SHOPPING).click()

    def click_checkout(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()
