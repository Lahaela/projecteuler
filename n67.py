#Problem 67

import numpy as np

triangle = np.zeros(100)

hand = open('p067_triangle.txt')
for line in hand:
	m = line.split()
	for i in range(100-len(m)):
		m.append(0)
	m = [int(el) for el in m]
	triangle = np.c_[triangle, m]

triangle = np.transpose(triangle)

for idx in reversed(range(100)): #skip the last line so not out of bounds
	row = triangle[idx]
	lowerrow = triangle[idx+1]
	for el in range(len(row)):
		if row[el]!=0:
			row[el] += max(lowerrow[el],lowerrow[el+1])

print(triangle[1])