import random

original_prices = [random.randint(-100, 100)for _ in range(5)] #В Python нижнее значение _использует переменное имя, когда само значение внутри цикла нам не нужно

new_prices = original_prices[:]

for i in range(len(original_prices)):

    if new_prices[i] < 0:

        new_prices[i] = 0

print("Исходные цены:", original_prices)
print("Новые цены:   ", new_prices)
print("Мы потеряли: ", sum(new_prices) - sum(original_prices))