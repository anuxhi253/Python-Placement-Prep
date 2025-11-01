num = int(input("Enter number: "))
rev = 0
while num:
    rev = rev * 10 + num % 10
    num //= 10
print("Reversed:", rev)
