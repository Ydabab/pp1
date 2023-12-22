def nth_prime_number(n):
    primes = [2]
    num = 3
    while len(primes) < n:
        for p in primes:
            if num % p == 0:
                break
        else:
            primes.append(num)
        num += 2
    return primes[-1]

print(nth_prime_number(5))