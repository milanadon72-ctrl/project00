films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']

count = int(input('Сколько фильмов хотите добавить? '))
listfilmnew = []

while len(listfilmnew) < count:
    movie = input(f"Введите название фильма: ")

    if movie in films:
        listfilmnew.append(movie) 
    else:
        print(f"Ошибка: фильма {movie} у нас нет :(")

print("Ваш список любимых фильмов: ", ", ".join(listfilmnew )) #вклеивает их в одну большую строку