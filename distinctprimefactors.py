import math

def primeFactors(n):
	factors = []
	buff = n
	while n % 2 == 0:
		n = n / 2
		factors.append(2)

	while isPrime(n) == False:
		for x in range(3, int(math.ceil(math.sqrt(n))+1), 2):
			if n % x == 0:
				factors.append(x)
				n = n / x

	factors.append(int(n))

	# if len(factors) > len(set(factors)):
	#     for x in range(0, len(factors)):
	#         for y in range (x+1, len(factors)):
	#             if factors[x] == factors[y]:
	#                 buff = factors[x]
	#                 factors.remove(buff)
	#                 factors.remove(buff)
	#                 factors.append(buff*buff)
	#                 break

	if 1 in factors:
		factors.remove(1)
	return factors


def isPrime(n):
	if n == 2:
		return True

	if n % 2 == 0:
		return False

	for x in range(3, int(math.ceil(math.sqrt(n))+1), 2):
		if n % x == 0:
			return False

	return True
			
x = 1
y = 2
z = 3
u = 4
check = False

print(primeFactors(58562))
print(primeFactors(58563))
print(primeFactors(58564))
print(primeFactors(58565))


# while check == False:
# 	if len(set(primeFactors(x)).intersection(primeFactors(y))) < 1 and len(set(primeFactors(x)).intersection(primeFactors(z))) < 1 and len(set(primeFactors(x)).intersection(primeFactors(u))) < 1 and len(set(primeFactors(y)).intersection(primeFactors(z))) < 1 and len(set(primeFactors(y)).intersection(primeFactors(u))) < 1 and len(set(primeFactors(z)).intersection(primeFactors(u))) < 1 and isPrime(x) == False and isPrime(y) == False and isPrime(z) == False and isPrime(u) == False:
# 		if len(primeFactors(x)) == 4 and len(primeFactors(y)) == 4 and len(primeFactors(z)) == 4 and len(primeFactors(u)) == 4:
# 			print(x,y,z,u)
# 			check = True
# 		else:
# 			x = x+1
# 			y = y+1
# 			z = z+1
# 			u = u+1
# 	else:
# 		x = x+1
# 		y = y+1
# 		z = z+1
# 		u = u+1
# 		print(x,y,z,u)