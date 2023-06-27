x = int(input("Enter Grade: "))
y = int(input("Enter Level: "))
l = y

if x < 1 or x > 100:
    print("Error incorrect grade")
elif l == 1:
    if x >= 71 and x <= 100:
        print("Distinction")
    elif x >= 61  and x <=70:
        print("Merit")
    elif x >= 50  and x <=60:
        print("Pass")
    elif x <= 49 and x >= 1:
        print("Fail")
elif l == 2:
    if x >= 66 and x <= 100:
        print("Distinction")
    elif x >= 51  and x <=65:
        print("Merit")
    elif x >= 40  and x <=50:
        print("Pass")
    elif x <= 40 and x >= 1:
        print("Fail")







