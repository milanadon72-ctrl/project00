import random

team_1 = [round(random.uniform(5, 10), 2) for _ in range(20)]
team_2 = [round(random.uniform(5, 10), 2) for _ in range(20)]

winners = [max(player_1, player_2) for player_1, player_2 in zip(team_1, team_2)]

print('Вторая команда:', team_2)
print('Победители тура:', winners)
