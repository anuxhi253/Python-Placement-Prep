lst = list(map(int, input("Enter numbers: ").split()))
k = int(input("Enter k: "))
k = k % len(lst)
rotated = lst[-k:] + lst[:-k]
print("Rotated list:", rotated)
