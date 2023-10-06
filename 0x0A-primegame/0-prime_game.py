#!/usr/bin/python3
"""
Define isWineer function, a solution to the Prime Game problem
"""


def isWinner(x, nums):
    """Return list of prime numbers between 1 and n inclusive
        Args:
        n (int): upper boundary of range. lower boundary is always 1
    """
    def sieve_of_eratosthenes(max_n):
        sieve = [True] * (max_n + 1)
        sieve[0] = sieve[1] = False
        primes = []
        for p in range(2, int(max_n**0.5) + 1):
            if sieve[p]:
                primes.append(p)
                for i in range(p * p, max_n + 1, p):
                    sieve[i] = False
        return primes

    def canWin(n, primes):
        if n in primes:
            return True
        for p in primes:
            if n % p == 0:
                return True
        return False

    maria_wins = 0
    ben_wins = 0

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    for n in nums:
        if canWin(n, primes):
            if n % 2 == 0:
                maria_wins += 1
            else:
                ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
