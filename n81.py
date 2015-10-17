#Problem 81

import numpy as np

matrx = np.zeros(80)

hand = open('p081_matrix.txt')
for line in hand:
	m = line.split(',')
	m = [int(el) for el in m]
	matrx = np.c_[matrx, m]

matrx = np.transpose(matrx)

for ele in reversed(range(79)):
	matrx[80][ele] += matrx[80][ele+1]

for idx in reversed(range(80)): #skip the last line so not out of bounds
	row = matrx[idx]
	lowerrow = matrx[idx+1]
	for el in reversed(range(len(row))):
		if el==79:
			row[el] += lowerrow[el]
		else:
			row[el] += min(lowerrow[el],row[el+1])

print(matrx[1])