import numpy 

num = str(2**1000)
sum = 0

for x in range(0,len(str(num))):
	y = int(num[x])
	sum = sum + int(y)

print(sum)