from src.pages.blocks.LeftNavigationBlock import LeftNavigationBlock
from src.core.WebElement import WebElement


class CompanyInfoPage(LeftNavigationBlock):

    @staticmethod
    def xpath_title_info_page(name_company):
        title_name_company_text: WebElement = WebElement(
            r"//div[@class='client-list-header' and text()='" + name_company + "']")
        return title_name_company_text


