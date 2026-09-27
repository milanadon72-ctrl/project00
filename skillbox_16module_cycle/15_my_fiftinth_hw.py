numbers_count = int(input("Кол-во чисел: "))
numbers = []

for i in range(numbers_count):
    num = int(input("Число: "))
    numbers.append(num)

print(f"\nПоследовательность: {numbers}")

start_index = 0

while start_index < len(numbers):
    sub_list = numbers[start_index:]
    
    if sub_list == sub_list[::-1]:
        break 
    start_index += 1

needed_numbers = numbers[:start_index]
needed_numbers.reverse()
print(f"Нужно приписать чисел: {len(needed_numbers)}")
print(f"Сами числа: {needed_numbers}")