# Generator for Fibonacci sequence
def fibonacci(n=None):
    a, b = 0, 1  # Starting numbers for the Fibonacci sequence
    count = 0    # Counter to keep track of how many numbers have been generated

    while True:
        # If n is provided and we have generated n numbers, stop
        if n is not None and count >= n:
            break

        yield a  # Yield the next number in the sequence
        a, b = b, a + b  # Move to the next Fibonacci numbers
        count += 1  # Increment the count

# Using the generator for an infinite sequence (press Ctrl+C to stop execution if testing this)
fib_gen = fibonacci()

for i in range(10):  # Let's print the first 10 Fibonacci numbers
    print(next(fib_gen))

# Bonus: Generating a specific number of Fibonacci numbers (e.g., first 7)
print("\nLimited Fibonacci sequence (7 numbers):")
limited_fib_gen = fibonacci(7)
for num in limited_fib_gen:
    print(num)
