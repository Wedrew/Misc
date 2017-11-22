import itertools

#Here I define my functions that compute the different subsets
def permWithRep(seq):
	for x in range(1,len(string)+1):
		for p in itertools.product(seq, repeat=x):
			print("{"+",".join(p)+"}")

def permWithoutRep(seq):
	for x in range(1,len(string)+1):
		for p in itertools.permutations(seq, x):
			print("{"+",".join(p)+"}")

def combWithRep(seq):
	for x in range(1,len(string)+1):
		for p in itertools.combinations_with_replacement(seq, x):
			print("{"+",".join(p)+"}")

def combWithoutRep(seq):
	for x in range(1,len(string)+1):
		for p in itertools.combinations(seq, x):
			print("{"+",".join(p)+"}")

def powerSet(seq):
	print("∅")
	for x in range(1,len(string)+1):
		for p in itertools.combinations(seq, x):
			print("{"+",".join(p)+"}")

def isUnique(s):
    return len(set(s)) == len(s)

#Start program and display information
print("This program returns the subsets of a given set")
exit1 = False
exit2 = False
exit3 = False

#Get user input and exit iff the set passes
while exit1 != True:
	string = input("Enter at least 3 and at most 5 unique elements that are lower case: ")
	if(string.isalpha() and string.islower() and isUnique(string) and len(string) >= 3 and len(string) <= 5):
		print("Set intitialized")
		exit1 = True
	else:
		if(string.isalpha() != True):
			print("Make sure all elements are letters")
		elif(string.islower() != True):
			print("Make sure all elements are lower case")
		elif(isUnique(string) != True):
			print("Make sure all elements are unique")
		elif(len(string) <= 3):
			print("Make sure you have 3 or more elements")
		elif(len(string) >= 5):
			print("Make sure you have 5 or fewer elements")

#Determine which type of set to display
while exit2 != True:
	repetition = input("Is repetition allowed? y/n: ")
	order = input("Does order matter? y/n: ")
	if(repetition == 'y' and order == 'y'):
		permWithRep(string)
		exit2 = True
	elif(repetition == 'n' and order == 'y'):
		permWithoutRep(string)
		exit2 = True
	elif(repetition == 'y' and order == 'n'):
		combWithRep(string)
		exit2 = True
	elif(repetition == 'n' and order == 'n'):
		combWithoutRep(string)
		exit2 = True
	else:
		print("Incorrect entry")

#Determine whether to display power set or not
while exit3 != True:
	powSet = input("Would you like to print the power set? y/n: ")
	if(powSet == 'y'):
		powerSet(string)
		exit3 = True
	elif(powSet == 'n'):
		exit3 = True
	else:
		print("Incorrect entry")