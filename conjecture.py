#Rewrote my conjecture in python because it supports infinite precision
import time

def isprime(n):
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2: 
        return True    
    if not n & 1: 
        return False
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

status = True
counter = 0
num = int(input("Enter number: "))

while status:
	print(int(num))
	time.sleep(.04)
	if isprime(num):
		num = (num*num)-1
	else:
		if num%2 == 0:
			num/=2
		else:
			num = num+1
	counter = counter+1
	if num == 2:
		status = False
print(2)
print("It took", counter, "steps")