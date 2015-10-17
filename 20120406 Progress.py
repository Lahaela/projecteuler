roger = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 20, 21, 22, 24, 25, 28, 29, 34, 36, 42, 47, 48, 52, 55, 67, 79, 92, 97]
leah = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 16, 20, 22, 25, 29, 30, 34, 36, 40, 42, 44, 45, 48, 50, 52, 56, 63, 92, 97]
runique = []
lunique = []

for e in roger:
    if e not in leah:
        runique.append(e)
for p in leah:
    if p not in roger:
        lunique.append(p)
print runique
print lunique

# runique = [11, 15, 18, 21, 24, 28, 47, 55, 67, 79]
# lunique = [30, 40, 44, 45, 50, 56, 63, 120]