lst = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter target sum: "))
found = False
for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] + lst[j] == target:
            print("Pair:", (lst[i], lst[j]))
            found = True
if not found:
    print("No pair found")
