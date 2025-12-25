points = [[1, 1], [3, 3], [7, 7], [2, 2], [4, 4], [6, 6], [0, 0], [10, 10], [12, 12]]

def distance(x1,y1,x2,y2):
    return ((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)) ** 0.5

def nearestPoints(points):
    # p1 and p2 are the indexes in the points list
    p1, p2 = 0, 1 # Initial two points

    shortestDistance = distance(points[p1][0], points[p1][1],
        points[p2][0], points[p2][1]) # Initialise shortestDistance
    lst = []
    # Compute distance between every two points
    for i in range(len(points)-1):
        for j in range(i + 1, len(points)):
            d = distance(points[i][0], points[i][1],
                        points[j][0], points[j][1]) # Find distance

            if d == shortestDistance:
                    p1, p2 = i, j # Update p1, p2
                    lst.append([points[p1][0],points[p1][1]])
                    lst.append([points[p2][0],points[p2][1]])
            if d < shortestDistance:
                p1, p2 = i, j # Update p1, p2
                shortestDistance = d # New shortestDistance
                lst = []    # Reset lst to null
                lst.append([points[p1][0],points[p1][1]])  # Add new point pair
                lst.append([points[p2][0],points[p2][1]])
    return lst

def main():
    lst = nearestPoints(points)
    print(lst)
    print("The least distance is between:")
    for i in range(0,len(lst),2):
        print(f"-> the points ({lst[i][0]},{lst[i][1]}) and ({lst[i+1][0]},{lst[i+1][1]})")
       
main()