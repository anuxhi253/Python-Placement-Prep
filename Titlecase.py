s = input("Enter sentence: ")
words = s.split()
title_case = ' '.join(word[0].upper() + word[1:].lower() for word in words)
print(title_case)
