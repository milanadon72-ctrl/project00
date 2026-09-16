available_ingredients = ['томаты', 'пепперони', 'сыр', 'грибы', 'курица', 'бекон', 'оливки']

menu = int(input("Сколько ингредиентов хотите добавить? "))
zakaz = []

while len(zakaz) < menu:#работает пока ингредиентов в списке не меньше переменной меню
    ingredient = input("Введите ингридиенты: ")

    if ingredient in available_ingredients:
        zakaz.append(ingredient)
        
    else:
        print(f"Ингредиента {ingredient} нет.. :(")

print("Ваш состав пиццы:", ", ".join(zakaz))