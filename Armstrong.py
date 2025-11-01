num = int(input("Enter number: "))
temp = num
n = len(str(num))
sum_ = 0
while temp:
    sum_ += (temp % 10) ** n
    temp //= 10
print("Armstrong" if sum_ == num else "Not Armstrong")
