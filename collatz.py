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
       seq.append(x)    # Added line
    return seq

print(collatz_sequence(27))