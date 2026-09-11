quantity = int(input('Количество видеокарт: '))
list_videocart = []
list_videocartnew = []

for num in range(quantity):
    videocard = int(input(f"Видеокарта {num + 1}: "))
    list_videocart.append(videocard) 

max_videocard = max(list_videocart)

for card in list_videocart:
    if card != max_videocard:
        list_videocartnew.append(card)

print("\nСтарый список видеокарт:", list_videocart)
print("Новый список видеокарт:", list_videocartnew)