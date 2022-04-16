import random
from pprint import pprint
for x in range(1, 11):
    print()
    for y in range(1, 11):
        if y < 5:
            choices = [1, 2, 3]
            sign = random.choices(choices)
            print(sign, end=' ')
        else:
            print(1, end=' ')

coord = [(x, y) for x in range(5) for y in range(5)]
coord2 = [(x, y) for x in range(5, 10) for y in range(5, 10)]
print()
print(coord)
print(coord2)
print()

for y in range(1, 11):
    print()
    for x in range(1, 11):
        choice = random.choices(('8', ' '))
        if x < 6:
            print(choice, end=' ')
        else:
            print((x, y), end=' ')

print('''
''')
coor = [(x, y) for x in range(1, 11) for y in range(1, 11)]
coor_to_change = [(x, y) for x in range(1, 11) for y in range(1, 11)]

for i in range(1, 11):
    print()
    for h in range(1, 11):
        ind = coor.index((i, h))
        print(coor[ind], end=' ')

for x, y in coor:
    choice = random.choices(('8', ' '))
    index = coor.index((x, y))
    prev_index = coor.index((x, 11 - y))
    if y < 6:
        coor_to_change[index] = choice
    else:
        coor_to_change[index] = coor_to_change[prev_index]


# for i in range(10):
#     print()
#     for h in range(10):
#         print(coor_to_change[i * h], end=' ')
print('''
''')
