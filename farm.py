import random
import time
import keyboard
import datetime
from datetime import datetime

print("Здравствуйте!")
start_game = datetime.now()
print(f"Время начала игры: {start_game.strftime('%H:%M:%S')}")
possible_keys = ['enter', 'space','tab','backspace','esc','delete','end','page up', 'page down', 'up', 'down','left','right','shift','ctrl','alt' ]

num_rounds = random.randint(0,4)
reaction_times = []
for round in range(num_rounds):
    print(f'Раунд {round + 1}')
    wait_time=random.randint(0,3)
    time.sleep(wait_time)
    choice = random.choice(possible_keys)
    print(f'Нажмите клавишу - {choice}')
    while True:
        if keyboard.is_pressed(choice):
            break
end_game = datetime.now()
print(f"Время окончания игры: {end_game.strftime('%H:%M:%S')}")
total = end_game - start_game
print(f"Общее время в игре: {total.total_seconds():.2f} секунд")
