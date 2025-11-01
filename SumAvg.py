lst = list(map(int, input("Enter numbers: ").split()))
total = 0
for x in lst:
    total += x
avg = total / len(lst)
print("Sum:", total, "Average:", avg)
