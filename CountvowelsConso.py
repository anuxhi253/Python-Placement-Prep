s = input("Enter string: ").lower()
vowels = "aeiou"
v = c = 0
for ch in s:
    if ch.isalpha():
        if ch in vowels:
            v += 1
        else:
            c += 1
print("Vowels:", v, "Consonants:", c)
