kilograms = eval(input("Enter the amount of water in kgs:"))
initialTemperature = eval(input("Enter the initial temperature of the water:"))
finalTemperature = eval(input("Enter the final temperature of the water:"))

energy = kilograms * (finalTemperature - initialTemperature) * 4184

print("The energy required in joules is:", energy)
