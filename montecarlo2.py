import random 
import time
def random_walk(n):
    x,y=0,0
    z = 0
    for i in range(n):
        (dx,dy) = random.choice([(0,1),(0,-1),(1,0),(-1,0)])
        x += dx
        y += dy
    return(x,y) 

for i in range(25):
    walk = random_walk(100)
    z = abs(walk[0]) + abs(walk[1])
    print(walk, '[Distance]-> ', z)  

    if z <=5:
        print('You are close')
        
    elif z > 5 and z <= 10:
        print('You are alright')
    elif z > 10 and z <= 15:
        print('You are far')    
    else:
       print('take a cab!')
    time.sleep(1)         
 
