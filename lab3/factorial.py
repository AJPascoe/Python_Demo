# Task 2 - Factorial  
# 1.	Add a new file: Factorial.py and make it the startup file.  
# 2.	Ask the user to input an integer.
# 3.	Display the number's factorial using a while loop. 
# Note: the factorial of a number is that number multiplied by all the preceding numbers.
# 			The factorial of 5 is =  5 x 4 x 3 x 2 x 1 = 120  
# 		or if you like = 1 x 2 x 3 x 4 x 5
# 4.	Save and run.




n = int(input("Factorial Number: "))
x = 1
while n > 1:
    x = n * x
    n -= 1
    print(x) 