#Calculates the highest sum from top to bottom (adjacent numbers) uses file input
triangle= [[]]
with open('p067_triangle.txt') as f:
	triangle = [line.split() for line in f]

f.close()

for x in range(len(triangle)-2,-1,-1):
	newrow = []
	for y in range(0,len(triangle[x])):
		sum1 = triangle[x][y] + triangle[x+1][y]
		sum2 = triangle[x][y] + triangle[x+1][y+1]
		if sum1 >= sum2:
			newrow.append(sum1)
		else:
			newrow.append(sum2)

	triangle[x+1] = 0
	triangle[x] = newrow

#print(triangle[0][0])