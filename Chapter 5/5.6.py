#   (Conversion from miles to kilometers and kilometers to miles)
#   Write a program that displays the following two tables side by side
#   (note that 1 mile is 1.609 kilo- meters and that 1 kilometer is .621 mile)


print("Miles      Kilometres  |  Kilometres     Miles")
print()

miles = 1
kilometres_ = 20
while miles < 11:
    while kilometres_ < 66:
        kilometres = format(miles * 1.609, ".3f")
        miles_ = format(kilometres_ / 1.609, ".3f")
        print(miles, "        ", kilometres, "      | ", kilometres_, "           ", miles_)
        miles += 1
        kilometres_ += 1

        
    
