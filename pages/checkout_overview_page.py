from selenium.webdriver.common.by import By


class CheckoutOverviewPage:
    # --- Locators ---
    TITLE           = (By.CLASS_NAME, "title")
    ITEM_TOTAL      = (By.CLASS_NAME, "summary_subtotal_label")
    TAX             = (By.CLASS_NAME, "summary_tax_label")
    TOTAL           = (By.CLASS_NAME, "summary_total_label")
    FINISH_BUTTON   = (By.ID, "finish")
    CANCEL_BUTTON   = (By.ID, "cancel")

    def __init__(self, driver):
        self.driver = driver

    # --- Actions ---
    def is_loaded(self):
        return "checkout-step-two" in self.driver.current_url

    def get_title(self):
        return self.driver.find_element(*self.TITLE).text

    def get_item_total(self):
        return self.driver.find_element(*self.ITEM_TOTAL).text

    def get_tax(self):
        return self.driver.find_element(*self.TAX).text

    def get_total(self):
        return self.driver.find_element(*self.TOTAL).text

    def click_finish(self):
        self.driver.find_element(*self.FINISH_BUTTON).click()

    def click_cancel(self):
        self.driver.find_element(*self.CANCEL_BUTTON).click()
