lst = list(map(int, input("Enter numbers: ").split()))
max_ = min_ = lst[0]
for num in lst:
    if num > max_:
        max_ = num
    if num < min_:
        min_ = num
print("Max:", max_, "Min:", min_)
