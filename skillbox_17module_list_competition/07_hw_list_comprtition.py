vowels = ["а", "о", "у", "ы", "э", "е", "ё", "и", "ю", "я"]

world = input('Введите текст: ')

world_new = [x for x in world.lower() if x in vowels]

print(f"Список гласных букв: {world_new}\n"
      f"Длина списка: {len(world_new)}")