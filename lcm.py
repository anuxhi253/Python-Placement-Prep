import math
a = int(input("Enter first: "))
b = int(input("Enter second: "))
lcm = abs(a*b) // math.gcd(a, b)
print("LCM:", lcm)
