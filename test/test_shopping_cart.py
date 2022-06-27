import unittest

from page_object.product_page import ProductPage
from page_object.shipping_cart_page import ShoppingCartPage, ProductInfo

from webdriver_factory import WebDriverFactory


class ShoppingCartTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = WebDriverFactory.get_driver()
        self.product_page = ProductPage(self.driver)
        self.shopping_cart_page = ShoppingCartPage(self.driver)
        self.product_33 = ProductInfo(name='Samsung SyncMaster 941BW')
        self.product_47 = ProductInfo(name='HP LP3065')
        self.result_expected = []
        self.result_expected.append(self.product_33)
        self.result_expected.append(self.product_47)
        self.total_price_expected = '$606.00'


    def tearDown(self) -> None:
        """Действия после теста"""
        # Выполняется после каждого теста!
        # Сохраняем скриншот с именем каждого теста
        self.driver.save_screenshot('test-reports/' + self.id() + '.png')
        self.driver.close()

    def test_shopping_cart(self):
        """Отзывы работают"""
        self.product_page.open_product('33')
        self.product_page.clear_field_qty()
        self.product_page.send_keys_field_qty('2')
        self.product_page.click_add_to_cart_button()
        self.assertTrue(self.product_page.assert_success_message_add_to_cart(product_name='Samsung SyncMaster 941BW'))
        self.product_page.open_product('47')
        self.product_page.click_add_to_cart_button()
        self.assertTrue(self.product_page.assert_success_message_add_to_cart(product_name='HP LP3065'))
        self.shopping_cart_page.open()
        self.assertEqual(self.result_expected, self.shopping_cart_page.get_shopping_cart_result())
        self.assertEqual(self.total_price_expected, self.shopping_cart_page.get_total_price_shopping_cart())
        self.shopping_cart_page.clear_shopping_cart()
        self.assertTrue(self.shopping_cart_page.assert_message_cart_empty())






