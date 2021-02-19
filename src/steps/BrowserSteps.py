from selenium.webdriver.common.keys import Keys


class BrowserSteps:

    @staticmethod
    def scroll_down(driver):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # todo find better way to do this
    @staticmethod
    def scroll_up(driver):
        driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
