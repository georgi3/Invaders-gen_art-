import random
from PIL import Image, ImageDraw


rnd = lambda: random.randint(55, 256)  # random number picker
random_clr = lambda: (rnd(), rnd(), rnd())  # RGB random color picker

color_symmetry = []
COMPUTER_SCREEN = (2560, 800)


def create_square(border, draw, random_color, element, size):
    if element == int(size/2):  # middle block case
        draw.rectangle(border, random_color)
    elif element > int(size/2):  # over the half case
        draw.rectangle(border, color_symmetry.pop())
    else:  # pre half cases
        color_symmetry.append(random_color)
        draw.rectangle(border, random_color)


def create_invader(border, draw, size, blackness):
    invader_x0, invader_y0, invader_x1, invader_y1 = border
    square_size = (invader_x1 - invader_x0)/size

    black = (0, 0, 0)
    # black = (0, 43, 255)
    yellow = (255, 239, 0)
    blue = (0, 155, 255)
    blue_d = (0, 55, 255)
    random_colors = [random_clr(), random_clr(), random_clr(), *(black,)*blackness]
    # random_colors = [(0, 255, 255), (0, 255, 255), (0, 255, 255), *(black,) * blackness]
    # random_colors = [blue_d, yellow, *(black,) * blackness]
    # random_colors = [yellow, *(black,) * blackness]

    for y in range(size):
        element = 0
        for x in range(size):
            x0 = x * square_size + invader_x0
            y0 = y * square_size + invader_y0
            x1 = x0 + square_size
            y1 = y0 + square_size
            create_square((x0, y0, x1, y1), draw, random.choice(random_colors), element, size)
            element += 1


def main(size, invaders, dimension=2560, screen=(2560, 1600), n=1, blackness=3):
    original_img = Image.new('RGB', (dimension, dimension))
    # original_img = Image.new('RGB', (screen))
    draw = ImageDraw.Draw(original_img)
    invader_size = dimension / invaders
    padding = (invader_size/size)*2
    padding = 47
    for x in range(invaders):
        for y in range(invaders):
            x0 = x * invader_size# + padding/2
            y0 = y * invader_size #+ padding/2
            x1 = x0 + invader_size# - padding
            y1 = y0 + invader_size# - padding
            create_invader((x0, y0, x1, y1), draw, size, blackness)
    rndm = random.randint(0, 10)
    # original_img.save(f'./img/ivanka - {size, invaders, blackness}', format='PNG')
    original_img.show(f'nice_screen{rndm}.jpg')


# main(size=70, invaders=10, dimension=1900, blackness=100)
for _ in range(10):
    main(size=101, invaders=1, screen=COMPUTER_SCREEN, blackness=3)
