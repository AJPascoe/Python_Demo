# In part 1 of this lab you'll practice using Lists through a series of 7 small exercises in order to become familiar with Lists. 
# You'll work with the following List
# ages = [12,18,33,84,45,67,12,82,95,16,10,23,43,29,40,34,30,16,44,69,70,74,38,65,36,83,50,11,79,64,78,37,3,8,68,22,4,60,33,82,45,23,5,18,28,99,17,81,14,88,50,19,59,7,44,93,35,72,25,63,11,69,11,76,10,60,30,14,21,82,47,6,21,88,46,78,92,48,36,28,51]
# 1.	Record the length of the ages List in a variable (you'll need it later)
# Display the length.
# Test your code.
# 2.	Display these ages one on each line:
# Tip: Use a for loop to read each number. 
# Test your code
# 3.	Add one year to every age!
# Tip:	 	ages[n] is the nth element of ages. 
# To increase (say) element 2 you may do ages[2] += 1
# len(ages) will return the length of the ages List.
# Redisplay ages to test your code.
# 4.	Our code only takes into account those people in the age range of 16-65 (inclusively)
# Please delete all ages which are outside this range.
# Tip:	There are other ways of achieving this task but one way is to use a for loop that uses the 	len() function to examine each item and then use the del() function to remove an item 	at certain index. 
# Redisplay ages to test your code.
# 5.	Display the count of 16-25 year olds.
# Test your code.
# 6.	Invoke the sort method on the ages List. 
# Tip:	 Use this line of code:   ages.sort()
# Display the ages List to make sure they are sorted. 
# 7.	What proportion of ages fall between 16-25?
# Test your code by displaying this value.


ages = [12,18,33,84,45,67,12,82,95,16,10,23,43,29,40,34,30,16,44,69,70,74,38,65,36,83,50,11,79,64,78,37,3,8,68,22,4,60,33,82,45,23,5,18,28,99,17,81,14,88,50,19,59,7,44,93,35,72,25,63,11,69,11,76,10,60,30,14,21,82,47,6,21,88,46,78,92,48,36,28,51]

print(f"There are {len(ages)} entries")
for x in ages:
    print(f"{x} orinal")
    print(f"{x + 1} added year")

for x in ages:
    if x > 65 or x < 16:
        print(f"{x} here")
        ages.remove(x)
print(ages)

ages1 = [x for x in ages if 16<= x <= 65]
ages1.sort()
print(ages1)


ages2 = [x for x in ages if 16<= x <= 25]
ages2.sort()
print(ages2)