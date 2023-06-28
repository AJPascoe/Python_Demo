# c = 0 # counter
# vc = 0   # vowel counter
# word = input(": ")
# while c < len(word):
#     x = word[c] # amount of letters
#     if x.lower() in "aeiou":   # checks to see if any of the letters are vowels
#         vc += 1  # if so add 1 to vowel counter
#     c += 1  # updates counter with the amount of vowels from vc
# print(vc)

word = "hello"
vc = 0
c= 0
for l in word:
    if l.lower() in "aeiou":   # checks to see if any of the letters are vowels
        vc += 1  # if so add 1 to vowel counter
        c += 1  # updates counter with the amount of vowels from vc
print(vc)

