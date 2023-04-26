import draw_map 
import random
map = [[random.choice([True, False]) for _ in range(100)] for _ in range(100)]

iterations = 5
for iter in range(iterations):
    for i in range(len(map)):
        for j in range(len(map[0])):
            cnt = 0
            for i_l in range(i-1, min(len(map)-1, i+2)):
                for j_l in range(j-1, min(len(map)-1, j+2)):
                    if map[i_l][j_l]:
                        cnt+=1
            map[i][j] = cnt >= 5

draw_map.draw_img(map)


