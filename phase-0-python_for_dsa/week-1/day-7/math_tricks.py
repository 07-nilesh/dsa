print(float('inf'))  # positive infinity — initialize min values
print(float('-inf') )      # negative infinity — initialize max values
print(abs(-5))
print(pow(2,10))
print(2**10)
#floor Division cuts off everything after the decimal (floors it down to the nearest integer).
print(10//3)  # 3 — floor division (critical for binary search)
print(10%3)   # 1 — modulo
print(divmod(10,3)) # (3, 1) — quotient and remainder

# Bit operations (needed for some problems)
n=2
#n & 1: 2 in binary is 10. 1 is 01. 
#10 & 01 equals 00 (Output: 0), confirming it's even.
print(n&1)  # check if odd (1) or even (0)

# n >> 1: Shifts bits right by 1 (10 becomes 1), dividing by 2 (Output: 1).
print(n>>1) # divide by 2 (floor)

#n << 1: Shifts bits left by 1 (10 becomes 100), multiplying by 2 (Output: 4).
print(n<<1) # multiply by 2

# n & (n-1): 2 & 1 is 10 & 01 which equals 0. 
# This is the ultimate trick to check if a number is a power of 2 (if it drops to 0, it is!).
print(n & (n-1))  # clear lowest set bit
print(bin(n))  # binary string representation