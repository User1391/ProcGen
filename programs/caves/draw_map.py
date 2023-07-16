from PIL import Image
def draw(two_d_list):
    for i in range(len(two_d_list)):
        for j in range(len(two_d_list[0])):
            if two_d_list[i][j]:
                print('#', end='')
            else:
                print(' ', end='')
        print('')

def draw_img(two_d_list):
    # from https://stackoverflow.com/questions/20304438/how-can-i-use-the-python-imaging-library-to-create-a-bitmap
    img = Image.new('RGB', (len(two_d_list), len(two_d_list[0])), "black")
    pixels = img.load()
    for i in range(len(two_d_list)):
        for j in range(len(two_d_list[0])):
            if two_d_list[i][j]:
                pixels[i,j] = (255, 255, 255)

    img.show()

def draw_img_color(two_d_list):
    img = Image.new('RGB', (len(two_d_list), len(two_d_list[0])), "black")
    pixels = img.load()
    for i in range(len(two_d_list)):
        for j in range(len(two_d_list[0])):
            #print(two_d_list[i][j], "pixel")
            pixels[i, j] = two_d_list[i][j]

    img.show()
