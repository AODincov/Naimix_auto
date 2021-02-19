from selenium.webdriver.common.by import By


# todo разделить на 2 класса?
class WebElement:
    selector_type: str
    locator: str

    def __init__(self, xpath_or_selector: str) -> None:
        self.locator = xpath_or_selector
        self.selector_type = self.__is_xpath_or_selector(self.locator)

    @staticmethod
    def __is_xpath_or_selector(locator: str) -> str:
        if locator.startswith("r//") or locator.startswith("//"):
            return 'xpath'
        else:
            return 'css'

    def get(self):
        if self.selector_type == 'xpath':
            return [By.XPATH, self.locator]
        else:
            return [By.CSS_SELECTOR, self.locator]


