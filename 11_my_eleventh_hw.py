target_detail = input("Название детали: ")

# Создаем переменные для подсчета количества и общей стоимости
detail_count = 0
total_cost = 0

# Проходим по всему списку и ищем совпадения
for item in shop:
    if item[0] == target_detail:
        detail_count += 1       # Увеличиваем счетчик количества на 1
        total_cost += item[1]   # Прибавляем цену текущей детали к общей стоимости

# Выводим результат
print(f"Кол-во деталей — {detail_count}")
print(f"Общая стоимость — {total_cost}")