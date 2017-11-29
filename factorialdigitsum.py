def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)

num = str((factorial(100)))
sum = 0

for x in range(0,len(str(num))):
	p = int(num[x])
	sum = sum + int(p)

print(sum)