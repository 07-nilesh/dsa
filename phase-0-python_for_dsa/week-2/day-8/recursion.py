# Factorial
def factorial(n):
    if n <=1:       #base case
        return 1
    return n * factorial(n-1)       # recursive case
print(factorial(4))

# fibonacii shows why memory matters
def fib_slow(n):    # TC : O(2^n)
    if n<=1:
        return n
    return fib_slow(n-1)+fib_slow(n-2)
print(fib_slow(4))

#with memoization -O(n)
from functools import lru_cache
@lru_cache(maxsize=None)
def fib_fast(n):
    if n<=1:
        return n
    return fib_fast(n-1)+fib_fast(n-2)
print(fib_fast(9))

# power -shows divide and conquer
def power(base,exp):
    if exp ==0:
        return 1
    if exp %2==0:
        half=power(base,exp//2)
        return half*half
    # O(log n) — much faster than O(n)
    return base * power(base,exp-1)
print(power(3,2))
