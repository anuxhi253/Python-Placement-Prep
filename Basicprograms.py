# 1. Swap two numbers without using a third variable
a, b = 5, 10
a, b = b, a
print(a, b)

# 2. Factorial (loop & recursion)
def fact_iter(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

def fact_rec(n):
    return 1 if n == 0 else n * fact_rec(n-1)

print(fact_iter(5), fact_rec(5))

# 3. Reverse a number
n = 1234
rev = int(str(n)[::-1])
print(rev)

# 4. Palindrome number
n = 121
print("Palindrome" if str(n) == str(n)[::-1] else "Not Palindrome")

# 5. Fibonacci series (loop & recursion)
def fib_iter(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a+b
    print()

def fib_rec(n):
    if n <= 1: return n
    return fib_rec(n-1) + fib_rec(n-2)

fib_iter(7)
print([fib_rec(i) for i in range(7)])

# 6. GCD & LCM
import math
a, b = 12, 18
print("GCD:", math.gcd(a, b))
print("LCM:", abs(a*b)//math.gcd(a, b))

# 7. Armstrong number
n = 153
s = sum(int(d)**len(str(n)) for d in str(n))
print("Armstrong" if s == n else "Not Armstrong")

# 8. Prime numbers in range
for i in range(10, 31):
    if all(i % j != 0 for j in range(2, int(i**0.5)+1)):
        print(i, end=" ")
print()

# 9. Perfect number
n = 28
s = sum(i for i in range(1, n) if n % i == 0)
print("Perfect" if s == n else "Not Perfect")

# 10. Sum of digits
n = 1234
print(sum(int(d) for d in str(n)))
