valid_numbers = []

print("Введите 4 числа для IP-адреса (от 0 до 255):")

for i in range(4):
    while True: 
        user_input = input(f"Число {i + 1}: ")
        
        if user_input.isdigit():
            number = int(user_input)  
            
            if 0 <= number <= 255:
                print("Ошибка! Число должно быть от 0 до 255. Попробуйте еще раз.")
                valid_numbers.append(user_input)  
                break  
        else:
            print("Ошибка! Вы ввели не число. Введите цифры от 0 до 255.")

ip_address = "{}.{}.{}.{}".format(valid_numbers[0], valid_numbers[1], valid_numbers[2], valid_numbers[3])

print("\nВаш IP-адрес успешно создан!")
print(ip_address)
