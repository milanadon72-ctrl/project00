end = input('На каком диске должен лежать файл: ')
start = input('Требуемое расширение файла: ')

path = ('{start1}:/user/docs/folder/new_file.{end1}'.format
        (end1=end, start1=start))

if not path.endswith('txt'):
    print('диск не коректкн ')
elif not path.startswith('C'):
    print('расширение не коректно')
else:
    print('Путь корректен!')