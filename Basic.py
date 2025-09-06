# 1. Reverse a string
s = "placement"
print(s[::-1])

# 2. Check palindrome number
n = 121
print(str(n) == str(n)[::-1])

# 3. Factorial using recursion
def fact(n):
    return 1 if n == 0 else n * fact(n-1)

print(fact(5))
