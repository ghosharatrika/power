# Taking 2**x outside the loop to improve the performance of the code to prevent its calculation at each iteration

import timeit


X = 5
L = [2 ** i for i in range(7)]

start_time = timeit.default_timer()  # To get the time at which the calculation has started
if 2 ** X in L:
    print('At index', L.index(2 ** X))
else:
    print(X, 'not found')
elapsed_time = timeit.default_timer() - start_time  # To get how much time is taken to perform the task
print(f"Time taken to find index without 2**X outside the loop: {elapsed_time} seconds")


value = 2**X
start_time = timeit.default_timer()  # To get the time at which the calculation has started
if value in L:
    print('At index', L.index(value))
else:
    print(X, 'not found')
elapsed_time = timeit.default_timer() - start_time  # To get how much time is taken to perform the task
print(f"Time taken to find the index with 2^5 outside the loop: {elapsed_time} seconds")
