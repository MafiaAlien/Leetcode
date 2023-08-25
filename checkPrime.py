def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    max_divisor = int(num**0.5) + 1
    for d in range(3, max_divisor, 2):
        if num % d == 0:
            return False
    return True

def first_n_primes(n):
    """Return the first n prime numbers."""
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

# Examples:
if __name__ == '__main__':
    n = 3
    print(first_n_primes(n))  # [2, 3, 5]

    n = 7
    print(first_n_primes(n))  # [2, 3,