import unittest

from page_object.product_page import ProductPage
from webdriver_factory import WebDriverFactory


class ProductPageTest(unittest.TestCase):

    def setUp(self) -> None:
        """Действия до теста"""
        self.expected_name = 'Apple Cinema 30"'
        self.expected_brand = 'Apple'
        self.expected_code = 'Product 15'
        self.expected_price = '$110.00'
        self.expected_description =\
            'The 30-inch Apple Cinema HD Display delivers an amazing 2560 x 1600 pixel resolution.'
        self.driver = WebDriverFactory.get_driver()
        self.product_page = ProductPage(self.driver)
        self.product_page.open_product('42')

    def tearDown(self) -> None:
        """Действия после теста"""
        # Выполняется после каждого теста!
        # Сохраняем скриншот с именем каждого теста
        self.driver.save_screenshot('test-reports/' + self.id() + '.png')
        self.driver.close()

    def test_information(self):
        """Информация присутствует"""
        self.assertEqual(self.expected_name, self.product_page.get_text_name_product())
        self.assertIn(self.expected_brand, self.product_page.get_text_brand_product())
        self.assertIn(self.expected_code, self.product_page.get_text_code_product())
        self.assertEqual(self.expected_price, self.product_page.get_text_price_product())
        self.assertIn(self.expected_description, self.product_page.get_text_description_product())


