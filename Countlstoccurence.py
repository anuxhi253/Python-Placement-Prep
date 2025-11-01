lst = list(map(int, input("Enter numbers: ").split()))
count = {}
for x in lst:
    count[x] = count.get(x, 0) + 1
print(count)
