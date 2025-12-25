#   (Display the ASCII character table)
#   Write a program that displays the characters
#   in the ASCII character table from ! to ~. Display ten characters per line.
#   The characters are separated by exactly one space.


symbols_per_line = 10


i = 41
for i in range(41,135):
    print(chr(i-8), " ", end = '')
    if i % symbols_per_line == 0:
        print()
    i += 1
