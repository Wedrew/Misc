#Calculates different paths to one for the Collatz conjecture
def collatz_sequence(x):
    seq = [x]
    if x < 1:
       return []
    while x > 1:
       if x % 2 == 0:
         x = x / 2
       else:
         x = 3 * x + 1 
       seq.append(int(x))    # Added line
    return seq

size = input("Please enter size: ")
toplength = 0

for x in range(1,int(size)+1):
  if len(collatz_sequence(x)) > toplength:
    toplength = len(collatz_sequence(x))
    num = x

print("Greatest orbit from 1 to " + str(x) + " is " + str(toplength) + " coming from number " + str(num))