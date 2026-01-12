from sympy import isprime

# Start with an initial value of n, and continue increasing n
n = 1
while True:
    num = 2**n + 1
    if num > 1000000 and isprime(num):
        result = num
        break
    n += 1

print(result)
