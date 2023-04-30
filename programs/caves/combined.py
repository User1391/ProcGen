import cell_auto
import norm_path
import draw_map

map = [[False for _ in range(100)] for _ in range(100)]

map = cell_auto.cell_auto(5)
map = norm_path.norm_path(map)

draw_map.draw_img(map)
