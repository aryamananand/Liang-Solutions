import turtle as t

t.speed(0)
scale = 3
start = 0
i = 0
count = 1
iterations = 1
lineCount = 0 

while iterations <= 57:
    
    if iterations % 8 == 0:
        start += 10 * scale
        i = 0
        count -= 8
        lineCount += 1


        
    if lineCount % 2 == 0:
        
        while  count <= 8:

                

                
            if count % 2 != 0: #odd numbered square => BLACK

                t.begin_fill()
                t.color("black")
                t.goto(i,0 + start)
                t.right(45)
                t.pendown()
                t.circle(5 * scale * (2 ** 0.5),steps = 4)
                t.left(45)
                t.end_fill()
                t.penup()
                
                count += 1
                
                
            else: #even numbered square => WHITE
                
                t.goto(i,0 + start)
                t.right(45)
                t.pendown()
                t.circle(5 * scale * (2 ** 0.5),steps = 4)
                t.left(45)
                t.penup()

                count += 1
                
                
            i += 10 * scale 
        iterations += 1

    else:
        
        while  count <= 8:
                
            if count % 2 == 0: #even numbered square => BLACK

                t.begin_fill()
                t.color("black")
                t.goto(i,0 + start)
                t.right(45)
                t.pendown()
                t.circle(5 * scale * (2 ** 0.5),steps = 4)
                t.left(45)
                t.end_fill()
                t.penup()
                
                count += 1
                
                
            else: #odd numbered square => WHITE
                
                t.goto(i,0 + start)
                t.right(45)
                t.pendown()
                t.circle(5 * scale * (2 ** 0.5),steps = 4)
                t.left(45)
                t.penup()

                count += 1
                
                
            i += 10 * scale 
        iterations += 1

t.hideturtle()
