s = input("Enter string: ")
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
max_char = max(freq, key=freq.get)
print("Most frequent:", max_char)
