def passwordChecker(list="password,Password,password123,Password123,qwerty"):
    passwords= list.split(',')
    print(list)
    print(passwords)
    x = input("Enter Password: ")
    if x in passwords:
        print(f"Use a safer password '{x}' is compromised")
    else:
        print("Storng Password")

    
passwordChecker()

# if passwords == "password" or "Password" or "password123" or "Password123" or "qwerty":
#         print("Week Passoword")