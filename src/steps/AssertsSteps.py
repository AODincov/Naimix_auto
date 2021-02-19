from datetime import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select


class AssertsSteps:

    @staticmethod
    def assert_dropdown_div(driver, list_for_check, dropdown):
        list_in_dropdown = []
        len_list_in_dropdown = len(driver.find_elements(dropdown[0], dropdown[1]))
        while len_list_in_dropdown != 0:
            if len_list_in_dropdown == 1:
                list_in_dropdown.append(
                    driver.find_element(dropdown[0], dropdown[1]).get_attribute("innerHTML").splitlines()[0])
            else:
                list_in_dropdown.append(driver.find_element(dropdown[0], "(" + dropdown[1] + ")[" +
                                                            str(len_list_in_dropdown) + "]").get_attribute(
                    "innerHTML").splitlines()[0])
            len_list_in_dropdown -= 1
        assert list_in_dropdown.sort() == list_for_check.sort()

    @staticmethod
    def assert_dropdown_select(driver, list_for_check, dropdown):
        inputs = Select(driver.find_element(dropdown))
        input1 = len(inputs.options)
        for items in range(input1):
            inputs.select_by_index(items)
            time.sleep(1)

    @staticmethod
    def check_exists_element(driver, element):
        try:
            driver.find_element(element[0], element[1])
        except NoSuchElementException:
            return False
        return True

    @staticmethod
    def check_not_exists_element(driver, element):
        try:
            driver.find_element(element[0], element[1])
        except NoSuchElementException:
            return

    @staticmethod
    def check_validation_field(driver, element, not_correct_values, web_element_with_text_error):
        for i in not_correct_values:
            AssertsSteps.check_not_exists_element(driver, not_correct_values[i])
            driver.find_element(web_element_with_text_error)
