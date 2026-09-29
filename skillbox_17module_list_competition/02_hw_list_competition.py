fst_num = int(input('напишите число А: '))
sec_num = int(input('напишите число B: '))

list_AB = [x for x in range(fst_num, sec_num + 1) if x % 2 == 0]

print(list_AB)