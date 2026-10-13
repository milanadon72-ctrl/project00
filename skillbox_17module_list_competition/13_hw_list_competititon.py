def caensar_cipher(string, user_shift):
    chair_list = [(alphabet[(alphabet.index(sym) + user_shift)% 33] if sym != ' ' else ' ')for sym in string]
    new_str = ''
    for i_char in chair_list:
        new_str += i_char
    return new_str

alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
input_str = input('введите строку:')
shift = int(input('введите сдвиг:'))

output_str = caensar_cipher(input_str, shift)

print(output_str)