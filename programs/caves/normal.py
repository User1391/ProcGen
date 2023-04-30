import random
import draw_map
import numpy as np

# based on http://www.roguebasin.com/index.php/Basic_directional_dungeon_generation

map = [[False for _ in range(100)] for _ in range(100)]

length = 99
roughness = 40
windyness = 80
width_l = 3
width_r = 3
avg = 0
stddev = int(len(map[0])*0.01)
y = 0
x = int(len(map[0])/2)

for i in range(max(x-width_l, 0), min(x+width_r, len(map[0]))):
    map[i][y] = True

for cnt in range(length):
    y+=1
    if random.randint(0,100) <= roughness:
        width_l = width_l + round(np.random.normal(avg, stddev))
        width_r = width_r + round(np.random.normal(avg, stddev))
        if width_l < 3:
            width_l = 3
        if width_r < 3:
            width_r = 3

    if random.randint(0, 100) <= windyness:
        x = x + round(np.random.normal(avg, stddev))
        if x < 0:
            x = 0
        elif x > len(map[0])-3:
            x = len(map[0])-3

    for i in range(max(x - width_l, 0), min(x+width_r, len(map[0]))):
        map[i][y] = True

draw_map.draw_img(map)
