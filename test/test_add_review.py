import unittest


from page_object.product_page import ProductPage
from tools import tools

from webdriver_factory import WebDriverFactory


class AddReviewTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = WebDriverFactory.get_driver()
        self.product_page = ProductPage(self.driver)
        self.product_page.open_product('42')

    def tearDown(self) -> None:
        """Действия после теста"""
        # Выполняется после каждого теста!
        # Сохраняем скриншот с именем каждого теста
        self.driver.save_screenshot('test-reports/' + self.id() + '.png')
        self.driver.close()

    def test_review(self):
        """Отзывы работают"""
        self.product_page.click_tab_reviews()
        self.product_page.click_button_reviews_continue()
        self.assertTrue(self.product_page.assert_warning_message_rating())
        self.product_page.enter_text_field_your_name('John')
        self.product_page.enter_text_field_your_review(tools.generate_random_string(24))
        self.product_page.click_rating_5()
        self.product_page.click_button_reviews_continue()
        self.assertTrue(self.product_page.assert_warning_message_symbol())
        self.product_page.clear_field_your_review()
        self.product_page.enter_text_field_your_review(tools.generate_random_string(26))
        self.product_page.click_button_reviews_continue()
        self.assertTrue(self.product_page.assert_success_message_review())


