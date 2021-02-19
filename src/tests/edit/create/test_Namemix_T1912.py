from src.initalization.BaseTest import BaseTest
from src.pages.CompanyPage import CompanyPage
from src.steps.BaseSteps import BaseSteps


# АдминНаймикса/Компании/Добавить компанию Иностранную организацию - валидация
class Test_Namemix_T1912(BaseTest):
    __correct_name_company = "АвтотестОФ.,?!;:-()""«».фФwW1" + BaseSteps.den_random_str(3)
    __not_correct_name_company_to_short = BaseSteps.den_random_str(4)
    __not_correct_name_company_to_long = BaseSteps.den_random_str(251)

    __correct_short_name_company = "АвтотестСНК.,?!;:-()""«».фФwW1" + BaseSteps.den_random_str(3)
    __not_correct_short_name_company_to_short = BaseSteps.den_random_str(4)
    __not_correct_short_name_company_to_long = BaseSteps.den_random_str(101)

    __correct_ein = "778591896"
    __not_correct_ein_to_short = BaseSteps.den_random_int(8)

    __correct_adress_company = "-Кострома"
    __not_correct_adress_company_to_long = BaseSteps.den_random_str(251)

    __correct_fio = "aAfF1-"
    __not_correct_fio_to_long = BaseSteps.den_random_str(151)

    __correct_number = "9999999999"

    __correct_email = "Test@test.test"
    __not_correct_email_without_dot_in_domen = BaseSteps.den_random_str(3) + "@" + BaseSteps.den_random_str(10)
    __not_correct_email_to_long = BaseSteps.den_random_str(321)
    __not_correct_email_without_sim = BaseSteps.den_random_str(7) + "." + BaseSteps.den_random_str(3)
    __not_correct_email_with_null_in_name = BaseSteps.den_random_str(3) + " " + BaseSteps.den_random_str(
        3) + "@" + BaseSteps.den_random_str(7) + "." + BaseSteps.den_random_str(3)
    __not_correct_email_with_null_name = "@" + BaseSteps.den_random_str(7) + "." + BaseSteps.den_random_str(3)
    __not_correct_email_with_null_domen = BaseSteps.den_random_str(3) + "@"
    __not_correct_email_with_null_after_domen = BaseSteps.den_random_str(
        3) + "@" + BaseSteps.den_random_str(7) + "." + BaseSteps.den_random_str(3) + "  "

    __correct_promocode = "ATALL-5"
    __not_correct_promocode_not_exist = "ATal99999"
    __not_correct_promocode_chanel_in_arhive = "АТ"
    __not_correct_promocode_not_active = "ATALL-0"
    __not_correct_promocode_not_active_use = "ATUSE"

    __not_correct_commisions_min = "-0.01"
    __not_correct_commisions_max = "100.01"

    def test_namemix_t1912(self, resource):
        BaseTest.login(self, login="nmadmin", password="nmadmin123")
        CompanyPage.close_content_list_task(self.driver)
        CompanyPage.click_create_company_button(self.driver)
        CompanyPage.select_type_company(self.driver, "Иностранная организация")
        CompanyPage.assert_dropdown_business_registration_form(self.driver, ["Юридическое лицо",
                                                                             "Индивидуальный предприниматель",
                                                                             "Иностранная организация"])
        CompanyPage.assert_req_field(self.driver, "Официальное название компании", "Сокращенное название компании"
                                     , "Фактический адрес", "Категория", "Идентификационный номер работодателя (EIN)")
        CompanyPage.assert_not_req_field(self.driver, "ФИО контактного лица", "Телефон контактного лица", "ИНН",
                                         "E-mail контактного лица", "Промо-код")
        CompanyPage.assert_error_inputs_field(self.driver, "Введите официальное название компании",
                                              {self.__not_correct_name_company_to_short: "Минимальная длина строки 5 символов",
                                                  self.__not_correct_name_company_to_long: "Максимальная длина - 250 символов"})
        CompanyPage.assert_error_inputs_field(self.driver, "Введите сокращенное название компании",
                                              {self.__not_correct_short_name_company_to_short: "Минимальная длина строки 5 символов",
                                                  self.__not_correct_short_name_company_to_long: "Максимальная длина - 100 символов"})
        CompanyPage.assert_error_inputs_field(self.driver, "Введите EIN",
                                              {self.__not_correct_ein_to_short: "Количество введенных знаков должно быть 9"})
        CompanyPage.assert_error_inputs_field(self.driver, "Введите адрес компании",
                                              {
                                                  self.__not_correct_adress_company_to_long: "Максимальная длина - 250 символов"})
        CompanyPage.assert_error_inputs_field(self.driver, "Введите ФИО",
                                              {self.__not_correct_fio_to_long: "Максимальная длина - 150 символов"})
        CompanyPage.assert_error_inputs_field(self.driver, "Введите E-mail",
                                              {
                                                  self.__not_correct_email_without_dot_in_domen: "Введен некорректный email",
                                                  self.__not_correct_email_to_long: "Введен некорректный email",
                                                  self.__not_correct_email_without_sim: "Введен некорректный email",
                                                  self.__not_correct_email_with_null_in_name: "Введен некорректный email",
                                                  self.__not_correct_email_with_null_name: "Введен некорректный email",
                                                  self.__not_correct_email_with_null_domen: "Введен некорректный email",
                                                  self.__not_correct_email_with_null_after_domen: "Введен некорректный email"})
        CompanyPage.assert_error_inputs_field(self.driver, "Введите промо-код (при наличии)",
                                              {self.__not_correct_promocode_not_exist: "Введен неверный промо-код",
                                               self.__not_correct_promocode_chanel_in_arhive: "Акция в архиве или удалена",
                                               self.__not_correct_promocode_not_active: "Промокод не активен или удален",
                                               self.__not_correct_promocode_not_active_use: "Превышено количество активаций"})

        CompanyPage.assert_commission_field(self.driver,
                                            {#self.__not_correct_commisions_min: "Процентная ставка не может быть меньше 0%",
                                                self.__not_correct_commisions_max: "Процентная ставка не может превышать 100%"})
        CompanyPage.assert_checbox(self.driver)
