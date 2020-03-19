# [0, 1, 1, 2, 3, 5, 8, 13, 21]

cache = {0: 1, 1: 1}

# Nth Fibonacci solution using caching / memoization


def rec_fib(n):
    # base cases
    # if n == 0:
    #     return 1
    # if n == 1:
    #     return 1
    if n in cache:
        return cache[n]

    # if it's not in the cache, we must
    n_minus_1 = rec_fib(n-1)
    n_minus_2 = rec_fib(n-2)
    cache[n] = n_minus_1 + n_minus_2

    return cache[n]


print(rec_fib(999))

print(rec_fib(1000))
