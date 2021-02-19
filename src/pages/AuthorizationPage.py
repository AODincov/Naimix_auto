from src.core.WebElement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from src.pages.blocks.LeftNavigationBlock import LeftNavigationBlock


class AuthorizationPage:
    __login_button: WebElement = WebElement("//button")
    __email_input: WebElement = WebElement("//input[@placeholder='E-mail']")
    __password_input: WebElement = WebElement("//input[@placeholder='Пароль']")
    __login_cookie_button: WebElement = WebElement("#root > div.login__wrapper > div.login-cookie > div > "
                                                   "div.login-cookie__button")

    @staticmethod
    def open_login_page(driver):
        driver.get('https://nm-test.mmtr.ru/')
        driver.wait.until(ec.element_to_be_clickable(AuthorizationPage.__email_input.get()))

    @staticmethod
    def close_cookie_login(driver):
        driver.wait.until(ec.element_to_be_clickable(AuthorizationPage.__login_cookie_button.get())).click()

    @staticmethod
    def login(driver, login: str, password: str):
        driver.wait.until(ec.element_to_be_clickable(AuthorizationPage.__email_input.get())).send_keys(login)
        driver.wait.until(ec.element_to_be_clickable(AuthorizationPage.__password_input.get())).send_keys(password)
        driver.wait.until(ec.element_to_be_clickable(AuthorizationPage.__login_button.get())).click()
        driver.wait.until(ec.visibility_of_element_located(LeftNavigationBlock.block_base_path.get()))

    @staticmethod
    def is_open(driver):
        driver.wait.until(ec.visibility_of_element_located(AuthorizationPage.__login_button.get()))

    @staticmethod
    def full_login(driver, login: str, password: str):
        AuthorizationPage.open_login_page(driver)
        AuthorizationPage.close_cookie_login(driver)
        AuthorizationPage.is_open(driver)
        AuthorizationPage.login(driver, login, password)
