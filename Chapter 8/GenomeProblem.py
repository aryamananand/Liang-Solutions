GeneString = input("Enter the Genome String: ")


for k in range (0, len(GeneString)):
    a = GeneString.find("ATG")
    realGene = GeneString[a  + 3 : len(GeneString)]



    t = ''
    for i in range (0, len(realGene)):
        t += realGene[i]
        if t.count("TAG") == 1 and len((t[0 : t.find("TAG") ])) % 3 == 0:
            print(t[0 : t.find("TAG")])
            t = ''

        elif t.count("TAA") == 1 and len((t[0 : t.find("TAG")])) % 3 == 0:
            print(t[0: t.find("TAA")  ])
            t =''

        elif t.count("TGA") == 1 and len((t[0 : t.find("TAG")])) % 3 == 0:
            print(t[0: t.find("TGA")])
            t =''

    