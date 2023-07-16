# based on https://web.williams.edu/Mathematics/sjmiller/public_html/hudson/Dickerson_Terrain.pdfimport draw_map and the relevant wikipedia page
import random
import draw_map
from statistics import mean
import math
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

def getcolor(coords):
    return map[coords[0]][coords[1]]

def avgcolor(t1, t2, t3, t4):
    outcolor = [0, 0, 0]
    for col in [t1, t2, t3, t4]:
        for i in range(3):
            outcolor[i] += col[i]

    for i in range(3):
        outcolor[i] = round(outcolor[i] / 4)
    return tuple(outcolor)

# combines the 2 above functions to get avg color from coords
def avgclrfrmcrds(c1, c2, c3, c4):
    return avgcolor(getcolor(c1), getcolor(c2), getcolor(c3), getcolor(c4))

def squareHelper(depth, a, b, c, d, t):
    tempcolor = avgclrfrmcrds(a, b, c, d)
    tempcolor = list(tempcolor)
    for i in range(len(tempcolor)):
        tempcolor[i] += smoothval()
    map[t[0]][t[1]] = tuple(tempcolor)
    

# with lots of help from https://github.com/qiao/fractal-terrain-generator/blob/master/lib/terrain.js
def diamond_step(depth):
    maplen = len(map)
    terrainsize = maplen - 1
    numsegs = 1 << (depth - 1) # cool trick from the above link
    span = int(terrainsize / numsegs)
    half = int(numsegs / 2)
    for x in range(0, terrainsize, span):
        for y in range(0, terrainsize, span):
            # get our corners and middle
            print(terrainsize, x, y)
            ul = (x, y)
            ur = (x + span, y)
            md = (x + half, y + half)
            bl = (x, y + span)
            br = (x + span, y + span)
            
            rawcolor = avgclrfrmcrds(ul, ur, bl, br)
            outcolor = list(rawcolor)
            for i in range(len(outcolor)):
                outcolor[i] += smoothval()
            
            outcolor = tuple(outcolor)
            print(md[0], md[1])
            map[md[0]][md[1]] = outcolor

def square_step(depth):
    maplen = len(map)
    terrainsize = maplen - 1
    numsegs = 1 << (depth - 1) 
    span = int(terrainsize / numsegs)
    half = int(numsegs / 2)
    for x in range(0, terrainsize, span):
        for y in range(0, terrainsize, span):
            va = [x, y]
            vb = [x + half, y]
            vc = [x + span, y]
            vf = [x, y + half]
            vg = [x + half, y + half]
            vh = [x + span, y + half]
            vk = [x, y + span]
            vl = [x + half, y + span]
            vm = [x + span, y + span]

            # right of h
            vhr = [x + half * 3, y + half]
            if vhr[0] > terrainsize:
                vhr[0] = half

            # left of f
            vfl = [x - half, y + half]
            if vfl[0] < 0:
                vfl[0] = terrainsize - half

            # under l
            vlu = [x + half, y + half * 3]
            if vlu[1] > terrainsize:
                vlu[1] = half

            # above b
            vba = [x + half, y - half]
            if vba[1] < 0:
                vba[1] = terrainsize - half
            
        squareHelper(depth, va, vg, vk, vfl, vf)
        squareHelper(depth, va, vba, vc, vg, vb)
        squareHelper(depth, vc, vhr, vm, vg, vh)
        squareHelper(depth, vk, vg, vm, vlu, vl)


sz0, sz1 = len(map)-1, len(map[0])-1

# first, randomly set the four corner values
map[0][0], map[sz0][0], map[0][sz1], map[sz0][sz1] = ((random.randint(0, 256), random.randint(0,256), random.randint(0,256)) for _ in range(4))

maplength = len(map)
iternum = round(math.log(maplength -1) / math.log(2))

counter = 1
while counter < iternum:
    diamond_step(counter)
    square_step(counter)
    counter += 1

draw_map.draw_img_color(map)
