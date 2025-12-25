FinalList = input('Enter integers between 1 and 100:').split(' ')
for i in range (100):
    if str(i) in FinalList:
        occurence = FinalList.count(str(i))
        var = 'time'
        if occurence > 1:
            var = 'times'
        print(f"{i} occurs {occurence} {var}")
