import random

def random_walking(n):
    x,y = 0,0
    for i in range(n):
        (dx,dy) = random.choice([(0,1),(0,-1),(1,0),(-1,0)])
        x += dx
        y += dy
    return (x,y)

number_of_blocks = 50000

for blocks_walked in range(1,31):
    walking_distance = 0 
    for i in range(number_of_blocks):
        (x,y) = random_walking(blocks_walked) 
        distance = abs(x) + abs(y)
        if distance <= 4:
            walking_distance += 1
    walking_distance_percentage = float(walking_distance)  / number_of_blocks
    print('[Blocks walked] -> ', blocks_walked, ' / % -> [walking distance] -> ', 100*walking_distance_percentage)

