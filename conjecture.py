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

for x in range(2,1001):
	counter = 0
	if isprime(x):
		num = x
		while num != 2:
			if isprime(num):
				num = (num*num)-1
			elif num % 2 == 0:
				num /= 2
			else:
				num += 1
			counter += 1
		print(x, " took", counter, "steps")