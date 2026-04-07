from selenium.webdriver.common.by import By


class CheckoutCompletePage:
    # --- Locators ---
    TITLE           = (By.CLASS_NAME, "title")
    CONFIRMATION    = (By.CLASS_NAME, "complete-header")
    BACK_HOME       = (By.ID, "back-to-products")

    def __init__(self, driver):
        self.driver = driver

    # --- Actions ---
    def is_loaded(self):
        return "checkout-complete" in self.driver.current_url

    def get_title(self):
        return self.driver.find_element(*self.TITLE).text

    def get_confirmation_message(self):
        return self.driver.find_element(*self.CONFIRMATION).text

    def click_back_home(self):
        self.driver.find_element(*self.BACK_HOME).click()
