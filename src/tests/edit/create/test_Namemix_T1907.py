from src.initalization.BaseTest import BaseTest
from src.pages.CompanyPage import CompanyPage
from src.steps.BaseSteps import BaseSteps


# АдминНаймикса/Компании/Добавить компанию ЮЛ - кнопка "отменить"
class Test_Namemix_T1907(BaseTest):
    __short_name_company = "Тестовое сокращенное название компании " + BaseSteps.den_random_str(3)

    def test_namemix_t1907(self, resource):
        BaseTest.login(self, login="nmadmin", password="nmadmin123")
        CompanyPage.close_content_list_task(self.driver)
        CompanyPage.click_create_company_button(self.driver)
        CompanyPage.filed_req_field(self.driver,
                                    "Тестовое название компании " + BaseSteps.den_random_str(5),
                                    self.__short_name_company,
                                    "3778591896",
                                    "Тестовый адресс компании" + BaseSteps.den_random_str(5), "Аренда", None, None)
        CompanyPage.click_cancel_company_button(self.driver)
        CompanyPage.search_company_with_go_on_info(self.driver, self.__short_name_company, "Компания не создана")
