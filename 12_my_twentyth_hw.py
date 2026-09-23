violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

songs_count = int(input("Сколько песен выбрать? "))

totul_time = 0

for i in range(1, songs_count + 1):
    songs_name = input(f"Название {i}-й песни: ")
    for song in violator_songs:
        if song[0] == songs_name:
            totul_time += song[1]

print(f"Общее время звучания песен: {round(totul_time, 2)} минуты")