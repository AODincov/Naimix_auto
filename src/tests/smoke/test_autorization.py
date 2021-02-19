from src.initalization.BaseTest import BaseTest


class Test_authorization(BaseTest):

    def test_authorization(self, resource):
        BaseTest.login(self, login="admin@admin.ru", password="Aa123456")
