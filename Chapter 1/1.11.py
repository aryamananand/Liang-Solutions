yr0 = 312032486

birthrate = (365 * 24 * 3600) // 7
deathrate = (365 * 24 * 3600) // 13
migration = (365 * 24 * 3600) // 45

netchange = birthrate - deathrate + migration

yr1 = yr0 + netchange
yr2 = yr1 + netchange
yr3 = yr2 + netchange
yr4 = yr3 + netchange
yr5 = yr4 + netchange

print("Population will be:")
print("Year 1:", yr1)
print("Year 2:", yr2)
print("Year 3:", yr3)
print("Year 4:", yr4)
print("Year 5:", yr5)
