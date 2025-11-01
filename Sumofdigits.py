num = int(input("Enter number: "))
sum_ = 0
while num:
    sum_ += num % 10
    num //= 10
print("Sum of digits:", sum_)
