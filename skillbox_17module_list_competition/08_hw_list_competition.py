# TODO здесь писать код

numlist = int(input("Введите длину списка: "))

list_new = [1 if x % 2 == 0 else x % 5 for x in range(numlist)]

print('Результат: ', list_new)