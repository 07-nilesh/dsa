def sumOfDigit(n):
    if n<=9:
        return n
    rem=n%10
    div=n//10
    return sumOfDigit(div)+rem
print(sumOfDigit(213))
