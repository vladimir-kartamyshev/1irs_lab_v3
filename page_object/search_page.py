from dataclasses import dataclass
from decimal import Decimal
from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page_object.base_page import BasePage


def extract_decimal_price(text: str) -> Decimal:
    """Функция, которая извлекает из строки цену"""
    """Примеры:
    $110.00 $122.00
    Ex Tax: $90.00
    $98.00 $122.00
    Ex Tax: $80.00
    $122.00
    Ex Tax: $100.00"""

    # text == "$110.00 $122.00\nEx Tax: $90.00"
    split_by_lines: List[str] = text.split("\n")
    # split_by_lines == ["$110.00 $122.00", "Ex Tax: $90.00"]

    first_price_lines = split_by_lines[0].split(' ')
    # first_price == ["$110.00", "$122.00"]

    # Удаляем первый символ (доллар)
    first_price = first_price_lines[0][1:]
    # В случае 1,202.00 нужно убрать запятую.
    first_price_without_punctuation = first_price.replace(",", "")

    return Decimal(first_price_without_punctuation)


@dataclass
class ProductInfo:
    name: str
    price: Decimal


class SearchPage(BasePage):
    page_url = '/index.php?route=product/search'

    def get_url(self) -> str:
        """Открыть страницу продукта"""
        return self.page_url

    def get_search_field_header(self) -> WebElement:
        """Получаем элемент поле поиска в Header"""
        search_field_header = self.driver.find_element(By.NAME, 'search')
        return search_field_header

    def enter_text_search_field_header(self, text: str):
        """Пишем в поле поиска """
        self.get_search_field_header().send_keys(text)

    def clear_search_field_header(self):
        """Очищаем поле поиска"""
        self.get_search_field_header().clear()

    def get_search_button_header(self) -> WebElement:
        """Получаем элемент кнопки поиск в Header"""
        search_button_header = self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']")
        return search_button_header

    def click_search_button_header(self):
        """Жмем кнопку поиска"""
        self.get_search_button_header().click()

    def get_search_field_criteria(self) -> WebElement:
        """Получаем элемент поле поиска Criteria"""
        search_field_criteria = self.driver.find_element(By.ID, 'input-search')
        return search_field_criteria

    def enter_text_search_field_criteria(self, text: str):
        """Вводим текст в поле поиска по критериям"""
        self.get_search_field_criteria().send_keys(text)

    def clear_search_field_criteria(self):
        """Очищаем поле поиска по критериям"""
        self.get_search_field_criteria().clear()

    def get_search_button_field_criteria(self) -> WebElement:
        """Получаем элемент кнопка поиска Criteria"""
        search_button_field_criteria = self.driver.find_element(By.ID, 'button-search')
        return search_button_field_criteria

    def click_search_button_field_criteria(self):
        """Жмем кнопку поиска по критериям"""
        self.get_search_button_field_criteria().click()

    def assert_message_no_product_search_criteria(self) -> bool:
        """Проверяем сообщение - (нет товаров, которые соответствуют критериям поиска)"""
        WebDriverWait(self.driver,timeout=10).until(expected_conditions.presence_of_element_located((By.XPATH, '//p[contains(text(),"There is no product that matches the search criteria.")]')))
        return True


    def get_checkbox_search_in_product_descriptions(self) -> WebElement:
        """Получаем элемент чекбокса search_in_product_descriptions """
        checkbox_search_in_product_descriptions = self.driver.find_element(By.XPATH, '//input[@name="description"]')
        return checkbox_search_in_product_descriptions

    def click_checkbox_search_in_product_descriptions(self):
        """Кликаем чекбокс search_in_product_descriptions"""
        self.get_checkbox_search_in_product_descriptions().click()

    def get_search_results(self) -> List[ProductInfo]:

        products_tags = self.driver.find_elements(By.CLASS_NAME, 'product-thumb')

        # Заводим пустой массив, куда будем накапливать информацию о продуктах.
        products: List[ProductInfo] = []

        # Перебираем все найденные теги с классом product-thumb
        for product_div_tag in products_tags:
            # Внутри тега ищем тег <H4> — внутри него будет название продукта.
            name: str = product_div_tag.find_element(By.TAG_NAME, 'h4').text

            # Внутри тега ищем тег с классом price, внутри него будет информация о ценах.
            price: str = product_div_tag.find_element(By.CLASS_NAME, 'price').text

            # Создаем объект по модели продукта.
            product = ProductInfo(
                name=name,
                price=Decimal(extract_decimal_price(price))
            )

            # Добавляем объект продукта в общий массив с продуктами.
            products.append(product)

        return products

