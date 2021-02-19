import time

from selenium.webdriver.chrome import webdriver

from src.pages.CompanyInfoPage import CompanyInfoPage
from src.pages.blocks.LeftNavigationBlock import LeftNavigationBlock
from selenium.webdriver.support import expected_conditions as ec
from src.core.WebElement import WebElement


# Поиск и создание компаний
from src.steps.AssertsSteps import AssertsSteps
from src.steps.BaseSteps import BaseSteps
from src.steps.BrowserSteps import BrowserSteps


class CompanyPage(LeftNavigationBlock):
    __check_button: WebElement = WebElement(r"//button[text()='Проверить']")
    __dropdown_company_type_button: WebElement = WebElement(r"//i[@class='dropdown icon']")
    __cancel_button: WebElement = WebElement(r"//button[@class='ui basic button apply-buttons__cancel']")
    __create_company_button: WebElement = WebElement(r"//button")
    __info_about_customer_title: WebElement = WebElement(r"#root > div.layouts > div.layouts_content > div > "
                                                         "div.client-new__header > div")
    __close_content_button_with_load: WebElement = WebElement(
        r"#root > div.layouts > div:nth-child(3) > div > div > i.close.icon")
    __close_content_button: WebElement = WebElement(r"//*[@id='root']/div[2]/div[3]/div/div/i")
    __load_content_icon: WebElement = WebElement(
        r"#root > div.layouts > div:nth-child(3) > div > div > i.circle.notched.loading.icon")
    __close_load_content: WebElement = WebElement(r"#root > div.layouts > div:nth-child(3) > div > div > i.close.icon")
    __business_registration_form_dropdown: WebElement = WebElement(r"//div[@name='clientType']//div[@class='menu "
                                                                   r"transition']//span")
    __category_dropdown: WebElement = WebElement(r"//div[@name='categoryId']//div[@class='menu "
                                                 r"transition']")
    __option_for_dropdown: WebElement = WebElement(r"//div[@role='option']")
    __add_button: WebElement = WebElement(
        r"//span[text() = 'Добавить']")
    __official_name_company_input: WebElement = WebElement(
        r"//input[@placeholder='Введите официальное название компании']")
    __short_name_company_input: WebElement = WebElement(
        r"//input[@placeholder='Введите сокращенное название компании']")
    __ein_input: WebElement = WebElement(
        r"//input[@placeholder='Введите EIN']")
    __inn_input: WebElement = WebElement(r"//input[@placeholder='Введите ИНН']")
    __address_company_input: WebElement = WebElement(r"//input[@placeholder='Введите адрес компании']")
    __fio_ip_input: WebElement = WebElement(r"//input[@placeholder='Введите ФИО ИП']")
    __company_dropdown_button: WebElement = WebElement(
        r"//*[@id='root']/div[2]/div[2]/div/form/div[10]/div[2]/div[1]/i")
    __category_dropdown_button: WebElement = WebElement(
        r"//div[@name='categoryId']")
    __name_company_search_input: WebElement = WebElement(r"//input[@name='nameSubstringFilter']")
    __search_company_button: WebElement = WebElement(r"//span[text()='Найти']")
    __commisions_input: WebElement = WebElement(r"//input[@name= 'currentCommissionRate']")
    __need_insurance_checbox: WebElement = WebElement(
        r"//div[@class='ui fitted checkbox']//input[@name='insuranceAvailable']")
    __registry_payments_checbox: WebElement = WebElement(
        r"//div[@class='ui fitted checkbox']//input[@name='registryPaymentsAvailable']")
    __unsecured_orders_disable_checbox: WebElement = WebElement(
        r"//div[@class='ui fitted checkbox']//input[@name='ordersUnsecured']")
    __unsecured_orders__checbox: WebElement = WebElement(
        r"//input[@name='ordersUnsecured']/..")

    __limit_input: WebElement = WebElement(r"//div[@class='ui input']//input[@name = 'ordersLimit']")
    __limit_disable_input: WebElement = WebElement(r"//div[@class='ui disabled input']//input[@name = 'ordersLimit']")

    @staticmethod
    def xpath_field_for_comissions(value):
        __commisions: WebElement = WebElement(r"//input[@name= 'currentCommissionRate' and @value='" + value + "']")
        return __commisions

    @staticmethod
    def xpath_field_for_new_company(field):
        __xpath_field_new_company: WebElement = WebElement("//input[@placeholder='" + field + "']")
        return __xpath_field_new_company

    @staticmethod
    def xpath_for_company_in_search_table(short_name_company):
        __company_card_href: WebElement = WebElement(r"//a[text()='" + short_name_company + "']")
        return __company_card_href

    # todo переделать под возможность выбора элемента
    @staticmethod
    def xpath_for_select_category(select_field):
        __category_select: WebElement = WebElement(
            "//div[@class='visible menu transition']//div//span[text()='" + select_field + "']")
        return __category_select

    @staticmethod
    def xpath_for_select_type(type_company):
        #  __type_company: WebElement = WebElement(
        #     "r//div[@class='visible menu transition']//div[@role='option']//span[text()='" + type_company + "']")
        if type_company == "Индивидуальный предприниматель":
            __type_company: WebElement = WebElement(
                "#root > div.layouts > div.layouts_content > div > form > div:nth-child(1) > div.field.client-new__row-input > div > div.visible.menu.transition > div:nth-child(2)")
            return __type_company
        elif type_company == "Иностранная организация":
            __type_company: WebElement = WebElement(
                "#root > div.layouts > div.layouts_content > div > form > div:nth-child(1) > div.field.client-new__row-input > div > div.visible.menu.transition > div:nth-child(3) > span")
            return __type_company

    @staticmethod
    def xpath_for_check_error_field_new_company_in_name(namefield, text_error):
        __field: WebElement = WebElement(
            r"//input[@value='" + namefield + "']/../../div[text()='" + text_error + "']")
        return __field

    @staticmethod
    def xpath_for_check_error_field_new_company_inn(namefield, text_error):
        __field: WebElement = WebElement(
            r"//div[@value='" + namefield + "']/../..//div[text()='" + text_error + "']")
        return __field

    @staticmethod
    def xpath_for_check_error_field_new_company_name(namefield, text_error):
        __field: WebElement = WebElement(
            r"//div[contains(text(),'" + namefield + "')]/..//div[text()='" + text_error + "']")
        return __field

    @staticmethod
    def close_content_list_task(driver):
        if AssertsSteps.check_exists_element(driver, CompanyPage.__load_content_icon.get()):
            driver.wait.until(
                ec.element_to_be_clickable(CompanyPage.__close_content_button_with_load.get())).click()
        else:
            driver.wait.until(ec.presence_of_element_located(CompanyPage.__close_content_button.get()))
            driver.wait.until(ec.element_to_be_clickable(CompanyPage.__close_content_button.get())).click()

    @staticmethod
    def click_create_company_button(driver):
        driver.wait.until(ec.presence_of_element_located(CompanyPage.__create_company_button.get())).click()
        driver.wait.until(ec.visibility_of_element_located(CompanyPage.__info_about_customer_title.get()))

    @staticmethod
    def click_add_button_with_go_on_search_company(driver):
        try:
            time.sleep(2)
            driver.wait.until(ec.presence_of_element_located(CompanyPage.__add_button.get()))
            driver.wait.until(ec.element_to_be_clickable(CompanyPage.__add_button.get())).click()
        except Exception:
            driver.wait.until(ec.presence_of_element_located(CompanyPage.__add_button.get()))
            driver.wait.until(ec.element_to_be_clickable(CompanyPage.__add_button.get())).click()
        #заменить на лоадер
        time.sleep(2)
        driver.wait.until(ec.visibility_of_element_located(CompanyPage.__name_company_search_input.get()))

    @staticmethod
    def click_cancel_company_button(driver):
        driver.wait.until(ec.presence_of_element_located(CompanyPage.__cancel_button.get())).click()
        driver.wait.until(ec.visibility_of_element_located(CompanyPage.__search_company_button.get()))

    @staticmethod
    def assert_dropdown_business_registration_form(driver, list_for_check):
        AssertsSteps.assert_dropdown_div(driver, list_for_check,
                                         CompanyPage.__business_registration_form_dropdown.get())

    @staticmethod
    def assert_req_field(driver, *field):
        driver.wait.until(ec.presence_of_element_located(CompanyPage.__add_button.get())).click()
        for i in field:
            driver.wait.until(ec.visibility_of_element_located(
                CompanyPage.xpath_for_check_error_field_new_company_name(i, 'Обязательное поле').get()))

    @staticmethod
    def assert_error_inputs_field(driver, field, not_correct_field_with_error: dict):
        for i in not_correct_field_with_error.keys():
            value = i
            BrowserSteps.scroll_up(driver)
            BaseSteps.explicit_expected_element(driver, CompanyPage.xpath_field_for_new_company(field).get())
            driver.wait.until(ec.visibility_of_element_located(
                CompanyPage.xpath_field_for_new_company(field).get())).send_keys(i)
            BrowserSteps.scroll_down(driver)
            if field == 'Введите промо-код (при наличии)':
                driver.wait.until(ec.presence_of_element_located(CompanyPage.__check_button.get())).click()
            else:
                BrowserSteps.scroll_down(driver)
                driver.wait.until(ec.presence_of_element_located(CompanyPage.__add_button.get())).click()
            if field == "Введите ИНН":
                driver.wait.until(ec.visibility_of_element_located(
                    CompanyPage.xpath_for_check_error_field_new_company_inn(i,
                                                                            not_correct_field_with_error.get(i)).get()))
            else:
                if field == "Введите EIN":
                    value = str(i[:2] + '-' + i[2:])
                    return value
                driver.wait.until(ec.visibility_of_element_located(
                    CompanyPage.xpath_for_check_error_field_new_company_in_name(value,
                                                                                not_correct_field_with_error.get(
                                                                                    i)).get()))
            BrowserSteps.scroll_up(driver)
            BaseSteps.clear_input(driver, CompanyPage.xpath_field_for_new_company(field))

    @staticmethod
    def assert_not_req_field(driver, *field):
        driver.wait.until(ec.presence_of_element_located(CompanyPage.__add_button.get())).click()
        for i in field:
            AssertsSteps.check_not_exists_element(driver, CompanyPage.xpath_for_check_error_field_new_company_name(i,
                                                                                                                   'Обязательное поле').get())

    @staticmethod
    def filed_req_field(driver, official_name_company, short_name_company, inn, address_company, category, fio_ip, ein):
        if fio_ip is not None:
            driver.wait.until(ec.visibility_of_element_located(CompanyPage.__fio_ip_input.get())).send_keys(
                fio_ip)
        if official_name_company is not None:
            driver.wait.until(
                ec.visibility_of_element_located(CompanyPage.__official_name_company_input.get())).send_keys(
                official_name_company)
        if short_name_company is not None:
            driver.wait.until(ec.visibility_of_element_located(CompanyPage.__short_name_company_input.get())).send_keys(
                short_name_company)
        if inn is not None:
            driver.wait.until(ec.visibility_of_element_located(CompanyPage.__inn_input.get())).send_keys(inn)
        if address_company is not None:
            driver.wait.until(ec.visibility_of_element_located(CompanyPage.__address_company_input.get())).send_keys(
                address_company)
        if category is not None:
            driver.wait.until(ec.visibility_of_element_located(CompanyPage.__category_dropdown_button.get())).click()
            driver.wait.until(
                ec.visibility_of_element_located(CompanyPage.xpath_for_select_category(category).get())).click()
        if ein is not None:
            driver.wait.until(ec.visibility_of_element_located(CompanyPage.__ein_input.get())).send_keys(
                ein)

    @staticmethod
    def search_company_with_go_on_info(driver: webdriver, name_company, company):
        driver.wait.until(
            ec.visibility_of_element_located(CompanyPage.__name_company_search_input.get())).send_keys(
            name_company)
        driver.wait.until(ec.element_to_be_clickable(CompanyPage.__search_company_button.get())).click()
        if company == "Компания создана":
            if "ФИО ИП" in name_company:
                driver.wait.until(
                    ec.element_to_be_clickable(
                        CompanyPage.xpath_for_company_in_search_table("ИП " + name_company).get())).click()
                driver.wait.until(
                    ec.visibility_of_element_located(CompanyInfoPage.xpath_title_info_page("ИП " + name_company).get()))
            else:
                driver.wait.until(
                    ec.element_to_be_clickable(
                        CompanyPage.xpath_for_company_in_search_table(name_company).get())).click()
                driver.wait.until(
                    ec.visibility_of_element_located(CompanyInfoPage.xpath_title_info_page(name_company).get()))
        else:
            assert not AssertsSteps.check_exists_element(driver, CompanyPage.xpath_for_company_in_search_table(
                name_company).get())

    @staticmethod
    def select_type_client(driver):
        driver.wait.until(ec.element_to_be_clickable(CompanyPage.__company_dropdown_button.get()))
        driver.wait.until(ec.visibility_of_element_located(CompanyPage.xpath_for_select_category().get())).click()

    @staticmethod
    def select_type_company(driver, type_company):
        driver.wait.until(ec.visibility_of_element_located(CompanyPage.__dropdown_company_type_button.get()))
        driver.wait.until(ec.element_to_be_clickable(CompanyPage.__dropdown_company_type_button.get())).click()
        # todo переделать под выбор
        driver.wait.until(ec.visibility_of_element_located(CompanyPage.xpath_for_select_type(type_company).get()))
        driver.wait.until(ec.element_to_be_clickable(CompanyPage.xpath_for_select_type(type_company).get())).click()

    @staticmethod
    def assert_commission_field(driver, not_correct_field_with_error: dict):
        BrowserSteps.scroll_down(driver)
        # default
        driver.wait.until(ec.visibility_of_element_located(CompanyPage.xpath_field_for_comissions("4.5").get()))
        BaseSteps.clear_input(driver, CompanyPage.__commisions_input)
        for i in not_correct_field_with_error.keys():
            driver.wait.until(
                ec.visibility_of_element_located(CompanyPage.__commisions_input.get())).send_keys(i)
            driver.wait.until(ec.presence_of_element_located(CompanyPage.__add_button.get())).click()
            driver.wait.until(ec.visibility_of_element_located(
                CompanyPage.xpath_for_check_error_field_new_company_in_name(i,
                                                                            not_correct_field_with_error.get(
                                                                                i)).get()))
            BaseSteps.clear_input(driver, CompanyPage.xpath_field_for_comissions(i))

    @staticmethod
    def assert_checbox(driver):
        driver.find_element(CompanyPage.__unsecured_orders_disable_checbox.get()[0],
                            CompanyPage.__unsecured_orders_disable_checbox.get()[1])
        driver.find_element(CompanyPage.__need_insurance_checbox.get()[0],
                            CompanyPage.__need_insurance_checbox.get()[1])
        driver.find_element(CompanyPage.__registry_payments_checbox.get()[0],
                            CompanyPage.__registry_payments_checbox.get()[1])
        driver.find_element(CompanyPage.__limit_disable_input.get()[0],
                            CompanyPage.__limit_disable_input.get()[1])
        driver.find_element(CompanyPage.__unsecured_orders__checbox.get()[0],
                            CompanyPage.__unsecured_orders__checbox.get()[1]).click()
        driver.find_element(CompanyPage.__limit_input.get()[0],
                            CompanyPage.__limit_input.get()[1])
