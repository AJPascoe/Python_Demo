#Write a program that takes three numberd as inputs: a, b, and c. 
#find the largest among the three numbers and perform the following:

#If the largest number is even, print "Even Number".
#If the largest number is odd and a multiple of 3, print "Odd Number and a Multiple of 3".
#If the largest number is odd and not a multiple of 3, print "Odd Number".

#DONT USE max(a,b,c): PROHIBITED!!

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))

if a > b and a > c:
    print("Number 1: ",a,"Is the largest")
    if a % 2 == 0:
        print("Number 1 also even")
    elif a % 3 == 0:
        print("Number 1 is the largest and odd and mutiple of 3")
    else:
        print("Number 1 is the largest and odd and not mutiple of 3")
elif b > a and b > c:
    print("Number 2: ",b,"Is the largest")
    if b % 2 == 0:
        print("Number 2 also even")
    elif b % 3 == 0:
        print("Number 2 is the largest and odd and mutiple of 3")
    else:
        print("Number 2 is the largest and odd and not mutiple of 3")
elif c > a and c > b:
    print("Number 3: ",c,"Is the largest")
    if c % 2 == 0:
        print("Number 3 also even")
    elif c % 3 == 0:
        print("Number 3 is the largest and odd and mutiple of 3")
    else:
        print("Number 3 is the largest and odd and not mutiple of 3")


## Tutors example ##

# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# c = int(input("Enter the third number: "))

# largest = a

# if b > largest:
#     largest = b
# if c > largest:
#     largest = c

# if largest % 2 == 0:
#     print("Even Number")
# elif largest % 2 != 0 and largest % 3 == 0:
#     print("Odd Number and a Multiple of 3")
# else:
#     print("Odd Number")