x = 1
y = 2
quit = True

while quit:
    if((x**2 + y**2) % (x+y) == 0):
        print(x, y)
        quit = False
    else:
        x=x+1
        y=y+1