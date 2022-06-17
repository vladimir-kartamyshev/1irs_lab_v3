import unittest
from decimal import Decimal

from page_object.search_page import SearchPage, ProductInfo
from webdriver_factory import WebDriverFactory


class SearchPageTest(unittest.TestCase):

    def setUp(self) -> None:
        """Действия до теста"""
        self.product_apple = ProductInfo(name='Apple Cinema 30"', price=Decimal('110.00'))
        self.product_sony = ProductInfo(name='Sony VAIO', price=Decimal('1202.00'))
        self.message_not_product = 'There is no product that matches the search criteria.'
        self.spisok_hp = {"name": 'HP LP3065', "price": '122.00'}
        self.spisok_imac = {"name": 'iMac', "price": '122.00'}
        self.product_hp = ProductInfo(name='HP LP3065', price=Decimal('122.00'))
        self.product_imac = ProductInfo(name='iMac', price=Decimal('122.00'))
        self.sdsd = self.product_hp.name
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
        self.search_page.get_search_field_header().send_keys('apple')
        self.search_page.get_search_button_header().click()
        self.assertIn(self.product_apple, self.search_page.get_search_results())

        self.search_page.get_search_field_header().clear()
        self.search_page.get_search_field_header().send_keys('sony')
        self.search_page.get_search_button_header().click()
        self.assertIn(self.product_sony, self.search_page.get_search_results())

        self.search_page.get_search_field_header().clear()
        self.search_page.get_search_field_header().send_keys('nokia')
        self.search_page.get_search_button_header().click()
        self.assertEqual(self.message_not_product, self.search_page.get_text_message_no_product_search_criteria())
