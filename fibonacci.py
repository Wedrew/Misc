def fibonacci(num):
	if num == 0:
		return 0
	elif num == 1:
		return 1
	else: 
		return fibonacci(num-1)+fibonacci(num-2)

x = input("How many iterations?: ")

for y in range(0,int(x)):
	print(fibonacci(y))