#inp = [[25, 2, 1, 100.5, 4, 320.5], [125, 2, 2, 40, 3, 85], [175, 2, 0, 125, 3, 75], [75, 1, 0, 125], [181, 1, 2, 125]]
n_and_lim = input("Enter number of banks and limit: ").split(' ')
n = int(n_and_lim[0])
limit = int(n_and_lim[1])

borrowers = [] # Create list 'borrowers' (each bank to each bank, hence a 'bank x bank' square matrix)
for a in range(int(n)):
    borrowers.append([])
    for b in range (int(n)):
        borrowers[a].append(0)


balance = []
for i in range(n):
    i_l = input(f"Bank {i}: ").split(' ')   # List for individual banks
    #i_l = inp[i]
    balance.append(float(i_l[0]))     # List of balances of banks
    a = 3
    for j in range(2,len(i_l)-1,2):  
        borrowers[i][int(i_l[j])] = float(i_l[j+1])
    
# print('i_l')
# print(i_l)

# print('Balance:')
# print(balance)
# print('')

# Calculate the banks' total assets... 

assets = []
for i in range(n):      # Create "assets" list
    assets.append(0)

print('Unsafe banks are: ', end = ' ')

var = []    # to prevent repetition in check loop
for m in range(n):
    var.append(0)

i = 0
while i < n:  # i is bank number
    asset_i = balance[i]      # Add balance to asset
    for j in borrowers[i]:
        asset_i += int(j)      # Add bank's loans to its asset
    assets[i] = asset_i   # Add bank i's asset to list 'assets
    if asset_i < limit:
        if var[i] == 0: # bank becomes unsafe for the first time
            var[i] = 1  # bank is now unsafe
            print(i, end = ' ')
            for k in range(n):
                borrowers[k][i] = 0     # Make loans from all banks to unsafe bank zero
            i = 0
        else:
            i += 1  # bank is already unsafe
    else:
        i += 1
t = 0
for j in var:
    t += j
if t == 0:
    print('None')



# print()

# print('balance: ', balance)
# print('Assets: ', assets)
# print('borrowers: ', borrowers)
