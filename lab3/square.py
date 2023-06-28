# Task1 - Squares
# 1.	Add a new file: Squares.py to your existing Solution and make it the startup file. 
# 2.	Write a while loop that starts at 1 and ends at 100.  
# 3.	Calculates and display each number and its square.  
# 4.	End the loop if that square is bigger than 2000.  
# 5.	Save and run.  



i = 1 

while i <= 100:
    s = i**2
    if s >=  2000:
        break
    print(i," x ",i, "=", s )
    i += 1