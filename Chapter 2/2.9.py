temperature = eval(input("Enter temperature in Fahrenheit between -58 and 41:"))

windspeed = eval(input("Enter the windspeed in miles per hour (minimum 2):"))

windChillIndex = 35.74 + 0.6215 * temperature - 35.75 * (windspeed) ** 0.16 + 0.4275 * temperature * (windspeed) ** 0.16


print("The wind chill index is:", windChillIndex)



