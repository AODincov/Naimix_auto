import random
from string import ascii_uppercase

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BaseSteps:

    @staticmethod
    def den_random_int(len_int):
        i = ''
        while len_int != 0:
            a = random.randint(0, 9)
            i += str(a)
            len_int -= 1
        return i

    @staticmethod
    def den_random_str(len_str):
        i = ''.join(random.choice(ascii_uppercase) for i in range(len_str))
        return i

    @staticmethod
    def select_from_dropdown(driver, dropdown_path, field):
        dropdown = Select(driver.find_element(dropdown_path))
        dropdown.select_by_visible_text(field)

    @staticmethod
    def clear_input(driver, web_element):
        driver.wait.until(ec.visibility_of_element_located(web_element.get())).send_keys(
            Keys.CONTROL + "a" + Keys.DELETE)

    @staticmethod
    def explicit_expected_element(driver, web_element):
        try:
            # Wait as long as required, or maximum of 5 sec for element to appear
            # If successful, retrieves the element
            WebDriverWait(driver, 5).until(
                ec.presence_of_element_located(web_element))
        except TimeoutException:
            print("Failed to load search bar at www.google.com")
