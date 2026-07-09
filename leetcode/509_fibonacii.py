class Solution:
    def fibonacii(n):  # lower runtime than lru_cache
        if n<=1:        # runtime 39 ms memory 19.20mb
            return n
        a,b=0,1
        for _ in range(2,n+1):
            a,b=b,a+b
        return b
print(Solution.fibonacii(5))

#with memoization -O(n) taked 53 ms
from functools import lru_cache
@lru_cache(maxsize=None)
def fib_fast(n):
    if n<=1:
        return n
    return fib_fast(n-1)+fib_fast(n-2)
print(fib_fast(9))