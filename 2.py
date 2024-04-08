def get_primes(min_val: int, max_val: int) -> list:
    sieve = [False if i % 2 == 0 else True for i in range(max_val)]
    primes = [2] if min_val <= 2 else []
    for p in range(3, max_val, 2):
        if sieve[p]:
            if p >= min_val:
                primes.append(p)
            for i in range(p * p, max_val, p * 2):
                sieve[i] = False
    return primes
