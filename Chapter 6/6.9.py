def footToMetre(foot):
    metre = 0.305 * foot
    return format(metre, ".3f")

def metreToFoot(metre):
    foot = metre / 0.305
    return format(foot, ".3f")

def main():
    print("Feet      Metres   |   Metres     Feet")
    print()
    foot = 1
    metre = 20
    while foot < 11:
        while metre <= 66:
            print(foot, "        ", footToMetre(foot), "   |   ", metre, "      ", metreToFoot(metre))
            if metre % 10 == 0:
                metre += 6
            else:
                metre += 4
            foot += 1

main()
                
    
