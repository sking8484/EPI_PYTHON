from typing import List

from test_framework import generic_test


# Given n, return all primes up to and including n.
def generate_primes(n: int) -> List[int]:
    primes = []
    is_prime = [False]*2 + [True]*(n-1)

    for prime in range(2,n+1):
        if is_prime[prime]:
            primes.append(prime)
            for mult in range(2*prime, n+1, prime):
                is_prime[mult] = False 

    return primes


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))
