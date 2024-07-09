import requests

# Получаем список категорий товаров
response = requests.get('https://fakestoreapi.com/products/categories')
categories = response.json()

print('Категории товаров:', categories)
chosen_category = input('Введите категорию товаров, которую хотите просмотреть: ')

# Получаем информацию о товарах выбранной категории
response = requests.get(f'https://fakestoreapi.com/products/category/{chosen_category}')
products = response.json()

# Выводим информацию о товарах выбранной категории
for product in products:
    print('\nНазвание товара:', product['title'])
    print('Описание:', product['description'])
    print('Цена:', product['price'])
    print('Количество оценок:', product['rating']['count'])
    print('Средний рейтинг:', product['rating']['rate'])
