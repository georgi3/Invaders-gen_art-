import random

coor = [[(x, y) for y in range(1, 11)] for x in range(1, 11)]
coor_to_change = [[(x, y) for y in range(1, 11)] for x in range(1, 11)]
row_i = 0
for row in coor:
    index = 0
    mirror_index = -1
    for x, y in row:
        choice = random.choices(('*', '*', ' ', ' '))
        if y < len(coor[0])+1:
            coor_to_change[row_i][index] = choice
            coor_to_change[row_i][mirror_index] = choice
        index += 1
        mirror_index -= 1
    row_i += 1

print(coor_to_change)
