n = [1, 2, 3]
k = int(input("Сдвиг: "))

k = k % len(n)

shifted_n = n[-k:] + n[:-k]

print("Изначальный список: ", n)
print("Сдвинутый список: ", shifted_n)