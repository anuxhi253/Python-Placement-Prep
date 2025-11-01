a = list(map(int, input("List A: ").split()))
b = list(map(int, input("List B: ").split()))
merged = a + b
merged.sort()
print("Merged & sorted:", merged)
