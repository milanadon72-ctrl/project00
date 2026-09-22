numbers = [1, 4, -3, 0, 10]

print(f"Изначальный список: {numbers}")
list_length = len(numbers)

for current_index in range(list_length):
    min_index = current_index
    
    for next_index in range(current_index + 1, list_length):
        if numbers[next_index] < numbers[min_index]:
            min_index = next_index
            
    numbers[current_index], numbers[min_index] = numbers[min_index], numbers[current_index]

print(f"Отсортированный список: {numbers}")