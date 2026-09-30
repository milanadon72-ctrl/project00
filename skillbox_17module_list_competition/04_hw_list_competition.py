import random

monster1 = [random.randint(50, 80) for _ in range(10) ]
monster2 = [random.randint(30, 60) for _ in range(10) ]
squad_uniti = ['погиб' if monster1[x]  + monster2[x] > 100
               else 'выжил' 
               for x in range(10)]

print(monster1)
print(monster2)
print(squad_uniti)