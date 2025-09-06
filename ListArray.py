arr = [10, 20, 4, 45, 99]

# 21. Largest & smallest
print(max(arr), min(arr))

# 22. Second largest
print(sorted(set(arr))[-2])

# 23. Sort without sort()
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
print(arr)

# 24. Sum of elements
print(sum(arr))

# 25. Remove duplicates
arr = [1, 2, 2, 3, 4, 4, 5]
print(list(set(arr)))

# 26. Missing number (1 to n)
nums = [1,2,3,5]
n = 5
print(set(range(1,n+1)) - set(nums))

# 27. Pair with given sum
arr = [2,7,11,15]; target = 9
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==target: print(arr[i],arr[j])

# 28. Intersection
a = [1,2,3]; b = [2,3,4]
print(list(set(a) & set(b)))

# 29. Rotate by k
arr = [1,2,3,4,5]; k=2
print(arr[k:]+arr[:k])

# 30. Majority element (>n/2)
arr = [2,2,1,1,2,2,2]
print(max(set(arr), key=arr.count))
