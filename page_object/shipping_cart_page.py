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


class ShoppingCartPage(BasePage):

    def get_url(self) -> str:
        page_url = '/index.php?route=checkout/cart'
        return page_url

    def get_shopping_cart_result(self) -> List[ProductInfo]:
        products_tags = self.driver.find_elements(By.ID, "checkout-cart")

        # Заводим пустой массив, куда будем накапливать информацию о продуктах.
        products: List[ProductInfo] = []

        # Перебираем все найденные теги
        for product_tag in products_tags:
            # Внутри тега ищем теги <//a[@href]//strong> — внутри них будет название продукта.
            names: List = product_tag.find_elements(By.XPATH, "//td[@class='text-left']//a[@href]")
            list_names = []
            for name in names:
                if name.text != '':
                    list_names.append(name.text)
            for name in list_names:

            # Создаем объект по модели продукта.
                product = ProductInfo(name=name)
            # Добавляем объект продукта в общий массив с продуктами.
                products.append(product)

        return products

    def get_button_remove(self) -> WebElement:
        """Получаем элемент кнопки удалить из корзины"""
        get_button_remove = self.driver.find_element(By.XPATH, "//button[@class='btn btn-danger']")
        return get_button_remove

    def click_button_remove(self):
        """Кликаем на кнопку удалить из корзины"""
        self.get_button_remove().click()
        WebDriverWait(self.driver, timeout=5).until(expected_conditions.invisibility_of_element(self.get_button_remove()))

    def get_message_cart_empty(self) -> WebElement:
        WebDriverWait(self.driver, timeout=5).until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@id='content']//p[text()='Your shopping cart is empty!']")))
        message_cart_empty = self.driver.find_element(By.XPATH, "//div[@id='content']//p[text()='Your shopping cart is empty!']")
        return message_cart_empty

    def assert_message_cart_empty(self) -> bool:
        message_cart_empty = self.get_message_cart_empty()
        text_message_cart_empty = message_cart_empty.text
        if text_message_cart_empty == 'Your shopping cart is empty!':
            return True

    def clear_shopping_cart(self):
        """Чистим корзину"""
        for i in self.get_shopping_cart_result():
            self.click_button_remove()

    def get_total_price_shopping_cart(self):
        tags_total_price_shopping_cart = self.driver.find_elements(By.XPATH, '//td[@class="text-right"]')
        total_price_shopping_cart = tags_total_price_shopping_cart[-1].text
        return total_price_shopping_cart





