from src.initalization.BaseTest import BaseTest
from src.pages.CompanyPage import CompanyPage
from src.steps.BaseSteps import BaseSteps


# АдминНаймикса/Компании/Добавить компанию ИП - валидация
class Test_Namemix_T1908(BaseTest):
    __correct_fio_ip = "АвтотестОФ.,?!;:-()""«».фФwW1" + BaseSteps.den_random_str(3)
    __not_correct_fio_ip_to_short = BaseSteps.den_random_str(4)
    __not_correct_fio_ip_to_long = BaseSteps.den_random_str(251)

    __correct_inn = "3778591896"
    __not_correct_inn_to_short = BaseSteps.den_random_int(11)
    __not_correct_inn = BaseSteps.den_random_int(12)

    __correct_adress_company = "-Кострома"
    __not_correct_adress_company_to_long = BaseSteps.den_random_str(251)

    __correct_fio = "aAfF1-"
    __not_correct_fio = BaseSteps.den_random_str(30)
    __not_correct_fio_to_long = "ыфвфывфывфывфывфыжвлфждэывпофужлдоимэдчалвомиэдфцлриэдылмирэдцрувтдэфывфывфцй-фывфывфы-фывфывфыфффыцц"

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

    def test_namemix_t1908(self, resource):
        BaseTest.login(self, login="nmadmin", password="nmadmin123")
        CompanyPage.close_content_list_task(self.driver)
        CompanyPage.click_create_company_button(self.driver)
        CompanyPage.select_type_company(self.driver, "Индивидуальный предприниматель")
        CompanyPage.assert_dropdown_business_registration_form(self.driver, ["Юридическое лицо",
                                                                             "Индивидуальный предприниматель",
                                                                             "Иностранная организация"])
        CompanyPage.assert_req_field(self.driver, "ФИО ИП",
                                     "ИНН", "Адрес регистрации", "Категория")
        CompanyPage.assert_not_req_field(self.driver, "ФИО контактного лица", "Телефон контактного лица", "ИНН",
                                         "E-mail контактного лица", "Промо-код")
        CompanyPage.assert_error_inputs_field(self.driver, "Введите ФИО ИП",
                                              {
                                                  self.__not_correct_fio_ip_to_short: "Минимальная длина строки 5 символов",
                                                  self.__not_correct_fio_ip_to_long: "Максимальная длина - 250 символов"})
        CompanyPage.assert_error_inputs_field(self.driver, "Введите ИНН",
                                              {self.__not_correct_inn_to_short: "ИНН может состоять только из 12 цифр",
                                               self.__not_correct_inn: "Неверный формат ИНН"})
        CompanyPage.assert_error_inputs_field(self.driver, "Введите адрес компании",
                                              {
                                                  self.__not_correct_adress_company_to_long: "Максимальная длина - 250 символов"})
        CompanyPage.assert_error_inputs_field(self.driver, "Введите ФИО",
                                              {self.__not_correct_fio_to_long: "Максимальная длина - 100 символов",
                                                  self.__not_correct_fio: "Только кириллица и знаки -"})
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
