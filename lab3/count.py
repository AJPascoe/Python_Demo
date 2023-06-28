# Task 3 - Count Vowels    
# 1.	Add a new file: CountVowels.py and make it the startup file.  
# 2.	Inputs a word (a string).
# 3.	Counts how many vowels are in the word.   
# Tip: You can scroll through every character of a string using its index.
# For example, if word =  'hello' then word[0] is the letter h and word[1] is the letter e.
# Use the len() function to find the length of a string. For example, in the above example,  	 len(word) is 5.
# Use simple if statement/s to detect if the character is 'a', 'e', 'i', 'o'  or  'u'.
# Every time you find a vowel you must increase a counter (an integer variable).
# In the next chapter (Lists) you'll discover a much easier way of performing this task.
# 4.	Save and run.

c = 0
vc = 0
word = input(": ")
while c < len(word):
    x = word[c]
    if x.lower() in "aeiou":
        vc += 1
    c += 1
print(vc)





# word = input(":")
    
# if "a" in word:
#     print("Yes A")
#     c += 1
#     print(c)
# elif "e" in word:
#     print("Yes E")
#     c += 1
#     print(c)
# elif "i" in word:
#     print("Yes I")
#     c += 1
#     print(c)
# elif "o" in word:
#     print("Yes O")
#     c += 1
#     print(c)
# elif "u" in word:
#     print("Yes U")
#     c += 1
#     print(c)
# else: 
#     print("no")
