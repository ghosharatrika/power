fibonacci_numbers = [0, 1]

while len(fibonacci_numbers) < 10:
    next_number = fibonacci_numbers[-1] + fibonacci_numbers[-2]
    fibonacci_numbers.append(next_number)

print(fibonacci_numbers)