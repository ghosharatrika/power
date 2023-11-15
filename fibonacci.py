fibonacci_numbers = [0, 1]


def generate_fibonacci(n):
    if n <= 0:
        print("Incorrect input")
    else:
        while len(fibonacci_numbers) < n:
            next_number = fibonacci_numbers[-1] + fibonacci_numbers[-2]
            fibonacci_numbers.append(next_number)
    return fibonacci_numbers
