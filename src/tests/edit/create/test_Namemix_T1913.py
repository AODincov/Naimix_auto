from src.initalization.BaseTest import BaseTest
from src.pages.CompanyPage import CompanyPage
from src.steps.BaseSteps import BaseSteps


# АдминНаймикса/Компании/Добавить компанию Иностранную организацию - кнопка "добавить"
class Test_Namemix_T1913(BaseTest):
    __short_name_company = "Тестовое сокращенное название компании " + BaseSteps.den_random_str(3)
    __correct_ein = "778591896"

    def test_namemix_t1913(self, resource):
        BaseTest.login(self, login="nmadmin", password="nmadmin123")
        CompanyPage.close_content_list_task(self.driver)
        CompanyPage.click_create_company_button(self.driver)
        CompanyPage.select_type_company(self.driver, "Иностранная организация")
        CompanyPage.assert_dropdown_business_registration_form(self.driver, ["Юридическое лицо",
                                                                             "Индивидуальный предприниматель",
                                                                             "Иностранная организация"])
        CompanyPage.assert_req_field(self.driver, "Официальное название компании", "Сокращенное название компании"
                                     , "Фактический адрес", "Категория", "Идентификационный номер работодателя (EIN)")
        CompanyPage.filed_req_field(self.driver,
                                    "Тестовое название компании " + BaseSteps.den_random_str(5),
                                    self.__short_name_company,
                                    None,
                                    "Тестовый адресс компании" + BaseSteps.den_random_str(5), "Аренда",
                                    None,
                                    self.__correct_ein)
        CompanyPage.click_add_button_with_go_on_search_company(self.driver)
        CompanyPage.search_company_with_go_on_info(self.driver, self.__short_name_company, "Компания создана")
