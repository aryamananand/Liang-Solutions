def convertMillis(millis):
    milli = millis % 1000
    seconds = millis // 1000

    minutes = seconds // 60 #Get minutes
    seconds = seconds % 60 #Get extra seconds

    hours = minutes // 60 #Get hours
    minutes = minutes % 60 #Get extra hours


    return f"{hours}:{minutes}:{seconds}.{milli}"

def main():
    n = eval(input("Enter time in milliseconds: "))
    print(convertMillis(n))
main()

