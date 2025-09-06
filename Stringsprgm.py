# 11. Reverse string without slicing
s = "hello"
rev = "".join(reversed(s))
print(rev)

# 12. Palindrome string
s = "madam"
print("Palindrome" if s == s[::-1] else "Not Palindrome")

# 13. Count vowels and consonants
s = "placement"
vowels = sum(1 for ch in s if ch.lower() in "aeiou")
consonants = len(s) - vowels
print(vowels, consonants)

# 14. Frequency of characters
s = "success"
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)

# 15. Duplicate characters
print([ch for ch in set(s) if s.count(ch) > 1])

# 16. Remove duplicates
s = "programming"
print("".join(sorted(set(s), key=s.index)))

# 17. Anagrams
s1, s2 = "listen", "silent"
print(sorted(s1) == sorted(s2))

# 18. First non-repeating character
s = "swiss"
for ch in s:
    if s.count(ch) == 1:
        print(ch); break

# 19. Title case without title()
s = "hello world from python"
print(" ".join(word[0].upper() + word[1:] for word in s.split()))

# 20. Longest word
s = "I am preparing for placements"
print(max(s.split(), key=len))
