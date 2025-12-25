import turtle as t
import random


screen = t.Screen()
screen.title('Self-Avoiding Random Walk')
screen.setup(width=330,height=330)
screen.setworldcoordinates(-6,-10,330,326)
# LIST FOR LATTICES
lst = []
for i in range(17):
    lst.append([])
    for j in range(17):
        lst[i].append(False)

# Code for grey grid
t.speed(0)  # Set the turtle speed to the fastest
t.tracer(0)
t.color('light gray')

for i in range(17):
    t.penup()
    t.goto(0,i*20)
    t.pendown()
    t.forward(320)

for j in range(17):
    t.penup()
    t.goto(j*20,0)
    t.left(90)
    t.pendown()
    t.forward(320)
    t.right(90)

t.color('blue')
t.width(2)
t.tracer(1)
t.speed(2)
# CODE TO AVOID lattice

x = 8
y = 8

lst[x][y] = True   # start point
t.penup()
t.goto(160,160)
t.pendown()
loop = True
while loop == True:
    final_path_list = []    # to append to this list the possible paths
    if x == 0 or x == 16 or y == 0 or y ==16:
        break
    if y < 16 and lst[x][y+1] == False:
        final_path_list.append(1)
    if x < 16 and lst[x+1][y] == False:
        final_path_list.append(2)
    if y > 0 and lst[x][y-1] ==  False:
        final_path_list.append(3)
    if x > 0 and lst[x-1][y] == False:
        final_path_list.append(4)
    if len(final_path_list) != 0:
        dir = random.randint(0,len(final_path_list)-1)     # to randomly select path from possibilities
        direction = final_path_list[dir]
    if len(final_path_list) == 0:
        break
    
    else:
        if direction == 1:      # upward 
            t.left(90)
            t.forward(20)
            t.right(90)
            lst[x][y+1] = True
            y += 1
        elif direction == 2:    # rightward 
            t.forward(20)
            lst[x+1][y] = True
            x += 1
        elif direction == 3:    # downward
            t.right(90)
            t.forward(20)
            t.left(90)
            lst[x][y-1] = True
            y -= 1
        elif direction == 4:   # leftward
            t.left(180)
            t.forward(20)
            t.right(180)
            lst[x-1][y] = True
            x -= 1
        
# print(lst)
t.hideturtle()
t.update()
t.done()
