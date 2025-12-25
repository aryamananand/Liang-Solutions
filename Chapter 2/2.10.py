speed = eval(input("Enter speed in m/s:"))
acceleration = eval(input("Enter acceleration in m/s^2:"))
runwayLength = (speed ** 2) / (2 * acceleration)

print("The minimum runway length for this aeroplane is:", runwayLength, "metres")
