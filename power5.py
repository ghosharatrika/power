# Using a for loop and the list append to generate powers of two and then finding 2^5

X = 5
L = [2 ** i for i in range(7)] 

if 2 ** X in L:
    print('At index', L.index(2 ** X))
else:
    print(X, 'not found')
