import unittest

from page_object.compare_page import ComparePage
from page_object.product_page import ProductPage


from webdriver_factory import WebDriverFactory


class CompareTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = WebDriverFactory.get_driver()
        self.product_page = ProductPage(self.driver)
        self.compare_page = ComparePage(self.driver)
        self.product_42 = 'Apple Cinema 30"'
        self.product_33 = 'Samsung SyncMaster 941BW'


    def tearDown(self) -> None:
        """Действия после теста"""
        # Выполняется после каждого теста!
        # Сохраняем скриншот с именем каждого теста
        self.driver.save_screenshot('test-reports/' + self.id() + '.png')
        self.driver.close()

    def test_compare(self):
        """Отзывы работают"""
        self.product_page.open_product('42')
        self.product_page.click_compare_this_product_button()
        self.assertTrue(self.product_page.assert_success_message_comparison(product_name=self.product_42))
        self.product_page.open_product('33')
        self.product_page.click_compare_this_product_button()
        self.assertTrue(self.product_page.assert_success_message_comparison(self.product_33))
        self.compare_page.open()
        self.compare_page.click_remove_button()
        self.compare_page.click_remove_button()
        self.assertTrue(self.compare_page.assert_message_not_chosen())



