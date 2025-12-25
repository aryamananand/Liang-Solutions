n = eval(input("Enter fibonacci index:"))
f0 = 0 # For fibs(0)
f1 = 1 # For fib(1)
for i in range(2, n + 1):
    currentFib = f0 + f1
    f0 = f1
    f1 = currentFib

print(currentFib)