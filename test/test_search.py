import unittest
from decimal import Decimal

from page_object.search_page import SearchPage, ProductInfo
from webdriver_factory import WebDriverFactory


class SearchPageTest(unittest.TestCase):

    def setUp(self) -> None:
        """Действия до теста"""
        self.product_apple = [ProductInfo(name='Apple Cinema 30"', price=Decimal('110.00'))]
        self.product_sony = [ProductInfo(name='Sony VAIO', price=Decimal('1202.00'))]
        self.product_hp = ProductInfo(name='HP LP3065', price=Decimal('122.00'))
        self.product_imac = ProductInfo(name='iMac', price=Decimal('122.00'))
        self.result_expected = []
        self.result_expected.append(self.product_hp)
        self.result_expected.append(self.product_imac)
        self.driver = WebDriverFactory.get_driver()
        self.search_page = SearchPage(self.driver)
        self.search_page.open()


    def tearDown(self) -> None:
        """Действия после теста"""
        # Выполняется после каждого теста!
        # Сохраняем скриншот с именем каждого теста
        self.driver.save_screenshot('test-reports/' + self.id() + '.png')
        self.driver.close()

    def test_search(self):
        """Поиск работает"""
        self.search_page.enter_text_search_field_header('Apple')
        self.search_page.click_search_button_header()
        self.assertEqual(self.product_apple, self.search_page.get_search_results())

        self.search_page.clear_search_field_header()
        self.search_page.enter_text_search_field_header('sony')
        self.search_page.click_search_button_header()
        self.assertEqual(self.product_sony, self.search_page.get_search_results())

        self.search_page.clear_search_field_header()
        self.search_page.enter_text_search_field_header('nokia')
        self.search_page.click_search_button_header()
        self.assertTrue(self.search_page.assert_message_no_product_search_criteria())

        self.search_page.clear_search_field_criteria()
        self.search_page.enter_text_search_field_criteria('stunning')
        self.search_page.click_checkbox_search_in_product_descriptions()
        self.search_page.click_search_button_field_criteria()
        self.assertEqual(self.result_expected, self.search_page.get_search_results())
