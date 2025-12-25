import random
import matplotlib.pyplot as plt

minLatticeSize = 10
maxLatticeSize = 80

ITERATIONS = 1000  # iterations per lattice size
FINALlist = []  #for plotting y values
x_latticeSize = []  #for plotting x values
for lattice_size in range(minLatticeSize,maxLatticeSize+1):
    count = 0
    for i in range (ITERATIONS):
        # LIST FOR LATTICES
        lst = []
        for i in range(lattice_size+1):
            lst.append([])
            for j in range(lattice_size+1):
                lst[i].append(False)

        # CODE TO AVOID lattice
        if lattice_size % 2 == 0:
            x = int(lattice_size/2)
            y = x
        else:
            x = int((lattice_size+1)/2)
            y = x

        lst[x][y] = True   # start point

        loop = True
        while loop == True:
            final_path_list = []    # to append to this list the possible paths
            if x == 0 or x == lattice_size or y == 0 or y ==lattice_size:
                break
            if y < lattice_size and lst[x][y+1] == False:
                final_path_list.append(1)
            if x < lattice_size and lst[x+1][y] == False:
                final_path_list.append(2)
            if y > 0 and lst[x][y-1] ==  False:
                final_path_list.append(3)
            if x > 0 and lst[x-1][y] == False:
                final_path_list.append(4)
            if len(final_path_list) != 0:
                dir = random.randint(0,len(final_path_list)-1)     # to randomly select path from possibilities
                direction = final_path_list[dir]
            if len(final_path_list) == 0:
                count += 1
                break
            
            else:
                if direction == 1:      # upward 
                    lst[x][y+1] = True
                    y += 1
                elif direction == 2:    # rightward 
                    lst[x+1][y] = True
                    x += 1
                elif direction == 3:    # downward
                    lst[x][y-1] = True
                    y -= 1
                elif direction == 4:   # leftward
                    lst[x-1][y] = True
                    x -= 1
    num = format((count/ITERATIONS)*100, ".2f")
    print(f"For a lattice of size {lattice_size}, the probabilty of dead-end paths is {num}%")
    FINALlist.append(num)
    x_latticeSize.append(lattice_size)


plt.figure(figsize=(7,7.5))
plt.rcParams['font.family'] = 'serif'
plt.plot(x_latticeSize, FINALlist, '-c')
plt.xlabel('Lattice Size')
plt.ylabel('Percentage of Dead-end Paths')
plt.title('Self-Avoiding Random Walk Dead-end Percentage')

plt.show()