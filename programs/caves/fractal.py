# based on https://web.williams.edu/Mathematics/sjmiller/public_html/hudson/Dickerson_Terrain.pdfimport draw_map and the relevant wikipedia page
import random
import draw_map
from statistics import mean
# dimensions must be a square with side length 2^n+1
map = [[(0, 0, 0) for _ in range(129)] for _ in range(129)]

# setup values
INITIAL_THRESHOLD = 1.0
DECAY = 0.5 # each iteration step multiplies the threshold by this level
SMOOTHING = 0.5 # decides smoothness of terrain, in range (0, 1) 

def colors(coords):
    return map[coords[0]][coords[1]]

def smoothval():
    return random.uniform(-1, 1) * pow(2, SMOOTHING * -1)

def diamond_step(c1, c2, c3, c4):
    if (c4[0]-c1[0] == 1):
        return
    mid = (int((c1[0]+c4[0]+1)/2 - 1), int((c1[1]+c4[1]+1)/2 - 1)) # midpoint coord pair from 2 coord. pairs
    print(mid)
    # now, pick which color we actually use
    red = int(mean([colors(c1)[0], colors(c2)[0], colors(c3)[0], colors(c4)[0]]) * smoothval())
    green = int(mean([colors(c1)[1], colors(c2)[1], colors(c3)[1], colors(c4)[1]]) * smoothval())
    blue = int(mean([colors(c1)[2], colors(c2)[2], colors(c3)[2], colors(c4)[2]]) * smoothval())
    map[mid[0]][mid[1]] = (red, green, blue)
    

sz0, sz1 = len(map)-1, len(map[0])-1

# first, randomly set the four corner values
map[0][0], map[sz0][0], map[0][sz1], map[sz0][sz1] = ((random.randint(0, 256), random.randint(0,256), random.randint(0,256)) for _ in range(4))

diamond_step((0,0), (sz0,0), (0,sz1), (sz0,sz1))

draw_map.draw_img_color(map)
