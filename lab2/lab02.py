## selection_part1 ##

# 1.	Add a new code page to your project. Call it selection_part1
# 2.	Create an IF statement to see if the person is equal 18 or over. 
# a.	Display 'You are in category A' 
# 3.	Create an IF statement to see if the person is equal 16 or over.
# a.	Display 'You are in category B' 
# 4.	Create another IF statement to see if the person is under 16 years of age.
# a.	Display 'You are in category C' 
# 5.	Save and run your code and enter 19 for age.
# 6.	As you see, there are too many confusing messages!
# Simple IF statements work fine but not in a chain of IF statements such as these.


# x = 9

# if x >= 18:
#     print("You are in category A")
# if x >= 16:
#     print("You are in category B")
# if x < 16:
#     print("You are in category C")

# 1.	Create an if…elif statement to examine the age in one statement. Follow this pattern:
# if person is 18 and over:
#        display message
# elif person is 16 and over:
#        	display message
# else:
# 	     display message
# Note: You must start with the highest age value first.
# 2.	Save and run your code using different values for age.

x = int(input("Please enter your age: "))

if x >= 18:
    print("You are in category A")
elif x >= 16:
    print("You are in category B")
elif x < 16:
    print("You are in category C")