def sieve_of_eratosthenes(n):
    # Initialize a list to track prime status of numbers
    primes = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        # If primes[p] is not changed, then it is a prime
        if primes[p]:
            # Updating all multiples of p to False
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    
    # Collecting all prime numbers
    prime_numbers = []
    for p in range(2, n + 1):
        if primes[p]:
            prime_numbers.append(p)
    
    return prime_numbers

# Example usage:
n = 50
print(f"Prime numbers up to {n}: {sieve_of_eratosthenes(n)}")


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(n):
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes

n = int(input("Enter a number: "))
primes = find_primes(n)
print("Prime numbers up to", n, "are:", primes)
