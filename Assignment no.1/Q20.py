# Prime finder: Loop 1-100, check primality with while/for, store in set, list primes in dict by digit sum.

primes = set()
for n in range(2, 101):
    for i in range (2, int(n**0.5)+1):
        if n % i == 0:
            break
    else:
        primes.add(n)

primes_by_sum = {}
for p in primes:
    s = sum(int(d) for d in str(p))
    primes_by_sum.setdefault(s, []).append(p)

print(primes_by_sum)