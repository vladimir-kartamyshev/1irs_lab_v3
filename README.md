# 1irs_lab

##Задание No 1. Тестирование страницы продукта
Открыть страницу http://54.183.112.233/index.php?route=product/product&product_id=42 Убедиться, что присутствует информация:
Название:Apple Cinema 30"
Бренд:Apple
ProductCode:Product 15
Цена:$110.00
Описание содержит предложение
“The30-inch Apple Cinema HD Display delivers anamazing 2560 x 1600 pixel”

##Задание No 2. Тестирование поиска
Открыть страницу
http://54.183.112.233/index.php?route=product/search
В поле поиска ввести “apple”, нажать кнопку “Поиск.”
В результатах поиска есть товар “AppleCinema 30"” и его стоимость равна $110.00.
В поле поиска ввести “sony”, нажать кнопку “Поиск” 
В результатах поиска есть товар “Sony VAIO” и его стоимость $1,202.00.
В поле поиска ввести “nokia”, нажать кнопку “Поиск” 
В результатах поиска сообщение “There is no product that matches the search criteria.
В поле “Search Criteria” ввести “stunning”, выбрать опцию “Search in product descriptions” и нажать кнопку “Search”
В результатах поиска два продукта: “HPLP3065”, “iMac”.

##Задание No3.Тестирование добавление отзыва на продукт
Открыть страницу
http://54.183.112.233/index.php?route=product/product&product_id=42
Открыть вкладку Reviews.
Не заполняя поля нажать кнопку Continue. Присутствует предупреждение “Warning: Please select a review rating!”
Выбрать любой рейтинг.
Ввести в поле Your Name “John”. Ввести в поле Your Review 24 символа. Нажать Continue.
Присутствует предупреждение “Warning: Review Text must be between 25 and 1000characters!” 
Ввести в поле Your Review текст больше 25 символов. Нажать Continue.Присутствует подтверждение: “Thank you for your review. It has been submitted to the webmaster for approval.”

##Задание No 4. Тестирование сравнения продуктов
Открыть страницу
http://54.183.112.233/index.php?route=product/product&product_id=42
Нажать кнопку “Compare this Product” 
Присутствует подтверждение: “Success: You have added Apple Cinema 30" to your product comparison!”
Открыть страницу
http://54.183.112.233/index.php?route=product/product&product_id=33
Нажать кнопку “Compare this Product”
Нажать ссылку “product comparison”
На странице сравнения продуктов два продукта: Apple Cinema 30" , Samsung SyncMaster 941BW
Удалить первый и второй товар из сравнения
На странице надпись “You have not any products to compare.”

##Задание No 5. Добавление продуктов в корзину
Открыть страницу
http://54.183.112.233/index.php?route=product/product&product_id=33
В поле Qty ввести 2.
Нажать кнопку Add to cart.
Присутствует подтверждение “Success: You have added Samsung SyncMaster 941BW to your shopping cart!”
Открыть страницу
http://54.183.112.233/index.php?route=product/product&product_id=47
Нажать кнопку Add to cart.
Присутствует подтверждение “Success: You have added HP LP3065 to your shopping cart!”
Открыть страницу
http://54.183.112.233/index.php?route=checkout/cart
В корзине два товара: Samsung SyncMaster 941BW , HP LP3065
Общая сумма Total: $606.00
Очистить корзину
Присутствует надпись: “Your shopping cart is empty!”


