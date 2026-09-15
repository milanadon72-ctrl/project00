quantity = input('Количество видеокарт: ')

vod = quantity.split()

num = []
for i in vod:
    num.append(int(i))

num.sort()

print("Новый список видеокарт:", num)