
x, y, z = eval(input("Enter three different integers: "))

'''

if (x < y < z) is True: 
    print (x,y,z)
elif (x < z < y) is True:
    print (x,z,y)
elif (y < x < z) is True:
    print(y,x,z)
elif (y < z < x) is True:
    print(y,z,x)
elif (z < x < y) is True:
    print(z,x,y)
else:
    print(z,y,x)





if x < y:
     smallest = x
if y < x:
    smallest = y
if z < smallest:
    smallest = z

print(smallest)

'''

'''
smallest = x

if y < smallest:
    smallest = y
if z < smallest:
    smallest = z
print(smallest)
'''


sum_ = x + y + z

#Smallest
smallest = x

if y < smallest:
    smallest = y

if z < smallest:
    smallest = z


#Biggest
biggest = x
if y > biggest:
    biggest = y

if z > biggest:
    biggest = z

medium = sum_ - (smallest + biggest)
 
    
print(smallest, medium, biggest)




