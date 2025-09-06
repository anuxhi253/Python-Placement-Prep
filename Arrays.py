# 4. Find largest element in a list
arr = [10, 20, 4, 45, 99]
print(max(arr))

# 5. Remove duplicates from list
arr = [1, 2, 2, 3, 4, 4, 5]
print(list(set(arr)))

# 6. Count frequency of characters in string
s = "success"
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)
