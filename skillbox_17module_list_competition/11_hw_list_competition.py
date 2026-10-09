input_string = input('Введите строку: ')

first_h_index = input_string.index('h')
last_h_index = input_string.rindex('h')

reversed_sequence = input_string[first_h_index + 1 : last_h_index][::-1]

print('Развёрнутая последовательность между первым и последним h:', reversed_sequence)
