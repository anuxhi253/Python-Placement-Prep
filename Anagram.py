s1 = input("Enter first: ")
s2 = input("Enter second: ")
print("Anagram" if sorted(s1) == sorted(s2) else "Not Anagram")
