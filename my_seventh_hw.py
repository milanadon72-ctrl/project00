world = input("Введите слово: ")

reversed_world = world[::-1] #переворачивает слово

if world == reversed_world:
    print("Слово является палиндромом")
else:
    print("Слово не является палиндромом")