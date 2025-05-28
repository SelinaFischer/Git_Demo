def find_primes(n):
    """Return a list of prime numbers up to n (inclusive)."""
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

def add_two_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b

# Example usage:
if __name__ == "__main__":
    print(find_primes(50))  # Prints all primes up to 50
    print(add_two_numbers(5, 7))  # Prints 12



