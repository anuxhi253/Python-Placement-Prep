lst = list(map(int, input("Enter numbers: ").split()))
non_zeros = [x for x in lst if x != 0]
zeros = [0] * (len(lst) - len(non_zeros))
result = non_zeros + zeros
print("After moving zeros:", result)
