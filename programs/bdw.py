import draw_map
import random

map = [[False for _ in range(100)] for _ in range(100)]

to_clear = 2000

i = random.randint(0,len(map))
j = random.randint(0,len(map[0]))
map[i][j] = True
to_clear -= 1
weights = [0.25, 0.25, 0.25, 0.25]
while to_clear > 0:
    ran_pick = random.choices([0, 1, 2, 3], weights=weights, k=1)[0] 
    c = [[0, 1], [0, -1], [1, 0], [-1, 0]][ran_pick]
    
    i += c[0]
    j += c[1]

    weights = [0.2, 0.2, 0.2, 0.2]
    weights[ran_pick] = 0.4

    if i < 0 or j < 0:
        i = max(i, 0)
        j = max(j, 0)
    elif i >= len(map) or j >= len(map[0]):
        i = min(i, len(map)-1)
        j = min(j, len(map[0])-1)

    if not map[i][j]:
        to_clear -= 1
        map[i][j] = True

draw_map.draw_img(map)
    

    

