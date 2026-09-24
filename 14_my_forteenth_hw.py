count_people = int(input("Кол-во человек: "))
drop_number = int(input("Какое число в считалке? "))
print(f"Значит, выбывает каждый {drop_number}-й человек\n")

people = list(range(1, count_people + 1))

start_index = 0

while len(people) > 1:
    print(f"Текущий круг людей: {people}")
    print(f"Начало счёта с номера {people[start_index]}")
    
    drop_index = (start_index + drop_number - 1) % len(people)
    
    print(f"Выбывает человек под номером {people[drop_index]}\n")
    
    people.pop(drop_index)
    
    start_index = drop_index % len(people)

print(f"Остался человек под номером {people[0]}")