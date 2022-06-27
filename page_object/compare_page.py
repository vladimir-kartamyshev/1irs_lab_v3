from dataclasses import dataclass
from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page_object.base_page import BasePage


@dataclass
class ProductInfo:
    name: str


class ComparePage(BasePage):

    def get_url(self) -> str:
        page_url = '/index.php?route=product/compare'
        return page_url

    # def get_compare_results(self) -> List[ProductInfo]:
    #     products_tags = self.driver.find_elements(By.XPATH, "//table[@class='table table-bordered']")
    #
    #     # Заводим пустой массив, куда будем накапливать информацию о продуктах.
    #     products: List[ProductInfo] = []
    #
    #     # Перебираем все найденные теги
    #     for product_div_tag in products_tags:
    #         # Внутри тега ищем тег <//a[@href]//strong> — внутри него будет название продукта.
    #         name: str = product_div_tag.find_element(By.XPATH, '//a[@href]//strong').text
    #         # Создаем объект по модели продукта.
    #         product = ProductInfo(
    #             name=name
    #         )
    #
    #         # Добавляем объект продукта в общий массив с продуктами.
    #         products.append(product)
    #
    #     return products

    def get_compare_results(self) -> List[ProductInfo]:
        products_tags = self.driver.find_elements(By.XPATH, '//a[@href]//strong')

        # Заводим пустой массив, куда будем накапливать информацию о продуктах.
        products: List[ProductInfo] = []

        # Перебираем все найденные теги
        for product_div_tag in products_tags:
            name = product_div_tag.text
            # Создаем объект по модели продукта.
            product = ProductInfo(
                name=name
            )

            # Добавляем объект продукта в общий массив с продуктами.
            products.append(product)

        return products

    def get_remove_button(self) -> WebElement:
        """Получаем элемент кнопки удалить из сравнения"""
        remove_button = self.driver.find_element(By.XPATH, "//a[@class='btn btn-danger btn-block']")
        return remove_button

    def click_remove_button(self):
        """Кликаем кнопку удалить из сравнения"""
        self.get_remove_button().click()

    def assert_message_not_chosen(self) -> bool:
        """Проверяем сообщение, что товаров в сравнении больше нет"""
        WebDriverWait(self.driver, timeout=10).until(expected_conditions.presence_of_element_located(
            (By.XPATH, "//div[@id='content']//p[text()='You have not chosen any products to compare.']")))
        return True
