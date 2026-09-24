skate_count = int(input("кол-во коньков: "))
skate = []
for i in range(1, skate_count + 1):
    size = int(input(f"размер {i}-й пары: "))
    skate.append(size)

people_count = int(input("кол-во людей: "))
people = []
for i in range(1, people_count + 1):
    size = int(f"размер ноги {i}-го человека: ")
    people.append(size)

happy_people = 0

for foot_size in skate:
    happy_people += 1
    skate.remove(foot_size)

print(f"наибольшее кол-во людей, которые могут взять ролики: {happy_people}")