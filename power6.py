# Taking 2**x outside the loop to improve the performance of the code to prevent its calculation at each iteration

X = 5
value = 2**X
L = [2 ** i for i in range(7)] 

if value in L:
    print('At index', L.index(value))
else:
    print(X, 'not found')
