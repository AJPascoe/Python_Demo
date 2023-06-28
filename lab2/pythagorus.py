s = input("Which side do you wish to calculate: ")

if s == "C" or "c":
    la = int(input("Length of A: "))
    lb = int(input("Length of B: "))

    print("Length of C is",(la * la)+ (lb *lb),"cm")
elif s == "A" or "a":
    lb = int(input("Length of B: "))
    lc = int(input("Length of C: "))
    print("Length of A is",(lc * lc)- (lb *lb),"cm")
elif s == "B" or "b":
    la = int(input("Length of A: "))
    lc = int(input("Length of C: "))
    print("Length of B is", (lc * lc)- (la *la),"cm")
else:
    print("Error")