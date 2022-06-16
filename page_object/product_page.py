from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

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



