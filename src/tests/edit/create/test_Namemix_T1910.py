from src.initalization.BaseTest import BaseTest
from src.pages.CompanyPage import CompanyPage
from src.steps.BaseSteps import BaseSteps


# АдминНаймикса/Компании/Добавить компанию ИП - кнопка "отменить"
class Test_Namemix_T1910(BaseTest):
    __fio_ip = "ФИО ИП" + BaseSteps.den_random_str(5)

    def test_namemix_t1910(self, resource):
        BaseTest.login(self, login="nmadmin", password="nmadmin123")
        CompanyPage.close_content_list_task(self.driver)
        CompanyPage.click_create_company_button(self.driver)
        CompanyPage.select_type_company(self.driver, "Индивидуальный предприниматель")
        CompanyPage.assert_dropdown_business_registration_form(self.driver, ["Юридическое лицо",
                                                                             "Индивидуальный предприниматель",
                                                                             "Иностранная организация"])
        CompanyPage.assert_req_field(self.driver, "ФИО ИП",
                                     "ИНН", "Адрес регистрации", "Категория")
        CompanyPage.filed_req_field(self.driver,
                                    None,
                                    None,
                                    "3778591896",
                                    "Тестовый адресс компании" + BaseSteps.den_random_str(5), "Аренда"
                                    , self.__fio_ip,None)
        CompanyPage.click_cancel_company_button(self.driver)
        CompanyPage.search_company_with_go_on_info(self.driver, self.__fio_ip, "Компания не создана")
