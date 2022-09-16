"""Computing primes."""


def sieve(n: int) -> list[int]:
    """
    Compute all the primes up to (and possibly including) `n`.

    `n` must be positive.

    >>> sieve(15)
    [2, 3, 5, 7, 11, 13]

    """
    assert n > 0
    candidates = list(range(2, n + 1))
    primes = []
    not_primes = []
    
    for i in candidates:
        if i in candidates:
            p = i
            primes.append(i)
            for j in candidates:
                if j % p == 0 and j != p:
                    candidates.remove(j)
 
    # FIXME: fill out this bit

    return primes


print(sieve(15))