from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page_object.base_page import BasePage


class ProductPage(BasePage):
    page_url = '/index.php?route=product/product&product_id='

    def open_product(self, product_id: str):
        """Открываем страницу продукта"""
        self.driver.get(self.get_base_url() + self.page_url + product_id)

    def get_name_product(self) -> WebElement:
        """Получаем элемент названия продукта"""
        name_product = self.driver.find_element(By.TAG_NAME, "h1")
        return name_product

    def get_text_name_product(self) -> str:
        """Получаем текст названия продукта"""
        text_name_product = self.get_name_product()
        return text_name_product.text

    def get_brand_product(self) -> WebElement:
        """Получаем элемент бренда продукта"""
        brand_product = self.driver.find_element(By.XPATH, "//div[@class='col-sm-4']//ul[1]//li[1]")
        return brand_product

    def get_text_brand_product(self) -> str:
        """Получаем текст бренда продукта"""
        text_brand_product = self.get_brand_product()
        return text_brand_product.text

    def get_code_product(self) -> WebElement:
        """Получаем элемент кода продукта"""
        code_product = self.driver.find_element(By.XPATH, "//li[starts-with(text(), 'Product Code: ')]")
        return code_product

    def get_text_code_product(self) -> str:
        """Получаем текст кода продукта"""
        text_code_product = self.get_code_product()
        return text_code_product.text

    def get_price_product(self) -> WebElement:
        """Получаем элемент цена продукта"""
        price_product = self.driver.find_element(By.XPATH, '//ul[@class="list-unstyled"]//li[h2]')
        return price_product

    def get_text_price_product(self) -> str:
        """Получаем текст цена продукта"""
        text_price_product = self.get_price_product()
        return text_price_product.text

    def get_description_product(self) -> WebElement:
        """Получаем элемент описание продукта"""
        description_product = self.driver.find_element(By.CLASS_NAME, 'tab-content')
        return description_product

    def get_text_description_product(self) -> str:
        """Получаем текст описание продукта"""
        text_description_product = self.get_description_product()
        return text_description_product.text

    def get_tab_reviews(self) -> WebElement:
        """Получаем элемент вкладки reviews"""
        tab_reviews = self.driver.find_element(By.XPATH, "//a[contains(text(), 'reviews')]")
        return tab_reviews

    def get_button_reviews_continue(self) -> WebElement:
        """Получаем элемент кнопки отправить отзыв"""
        button_reviews_continue = self.driver.find_element(By.ID, 'button-review')
        return button_reviews_continue

    def assert_warning_message_symbol(self) -> bool:
        """Проверяем предупреждение символы"""
        WebDriverWait(self.driver, timeout=10).until(expected_conditions.presence_of_element_located((By.XPATH, "//div[text()=' Warning: Review Text must be between 25 and 1000 characters!']")))
        return True

    def assert_warning_message_rating(self) -> bool:
        """Проверяем предупреждение рейтинг"""
        WebDriverWait(self.driver, timeout=10).until(expected_conditions.presence_of_element_located((By.XPATH, "//div[text()=' Warning: Please select a review rating!']")))
        return True

    def assert_success_message(self) -> bool:
        """Проверяем success сообщение"""
        WebDriverWait(self.driver, timeout=10).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '.alert.alert-success.alert-dismissible')))
        return True

    def get_field_your_name(self) -> WebElement:
        """Ищем поле ввода имени"""
        field_your_name = self.driver.find_element(By.ID, 'input-name')
        return field_your_name

    def enter_text_field_your_name(self, text: str):
        """Вводим текст в поле имя"""
        field_your_name = self.get_field_your_name()
        field_your_name.send_keys(text)

    def get_field_your_review(self) -> WebElement:
        """Ищем поле ввода отзыва"""
        field_your_review = self.driver.find_element(By.ID, 'input-review')
        return field_your_review

    def enter_text_field_your_review(self, text: str):
        """Вводим текст в поле отзыв"""
        text_field_your_review = self.get_field_your_review()
        text_field_your_review.send_keys(text)

    def click_rating_5(self):
        """Жмем кнопочку с рейтингом 5"""
        click_rating_5 = self.driver.find_element(By.XPATH, '//input[@type="radio"][@name = "rating"][@value=5]')
        click_rating_5.click()

    def clear_field_your_name(self):
        """Очищаем поле имя"""
        field_your_name = self.get_field_your_name()
        field_your_name.clear()

    def clear_field_your_review(self):
        """Очищаем поле отзыв"""
        field_your_review = self.get_field_your_review()
        field_your_review.clear()

