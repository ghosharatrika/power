L = [1, 2, 4, 8, 16, 32, 64]
X = 5
found = False
for index, val in enumerate(L):
    if 2 ** X == val:
        print('at index', index)
        break
else:
    print(X, 'not found')
