lst = list(map(int, input("Enter numbers: ").split()))
result = []
for x in lst:
    if x not in result:
        result.append(x)
print("Without duplicates:", result)
