def displaySortedNumbers(x, y, z):
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
     
        
    return (smallest, medium, biggest)

def main():
    x,y,z = eval(input("Enter three integers: "))
    print("The sorted integers are: ", displaySortedNumbers(x,y,z))
main()
