import requests

# Получаем информацию о первых 5 пользователях
response_users = requests.get('https://fakestoreapi.com/users?limit=5')
users = response_users.json()
print("Информация о первых 5 пользователях:")
for user in users:
    print(f"ID пользователя: {user['id']}")
    print(f"Имя пользователя: {user['name']}")

user_name = input('\nВведите свое имя или идентификатор пользователя: ')

# Получаем информацию о всех корзинах пользователей
response_carts = requests.get('https://fakestoreapi.com/carts')
carts = response_carts.json()

# Выводим информацию о корзинах пользователя
for cart in carts:
    if cart['userId'] == user_name:
        print(f"\nКорзина ID: {cart['id']}")
        print(f"Пользователь ID: {cart['userId']}")
        print("Товары в корзине:")
        for item in cart['products']:
            print(f"Название товара: {item['title']}")
            print(f"Цена: {item['price']}")
            print(f"Количество: {item['quantity']}")