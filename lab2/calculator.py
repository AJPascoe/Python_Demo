x = input("Select Operator: ")
num1 = int(input("First Number: "))
num2 = int(input("Second Number: "))

o = x

if x == "/":
    print(num1 / num2)
elif x == "*":
    print(num1 * num2)
elif x == "-":
    print(num1 - num2)
elif x == "+":
    print(num1 + num2)
elif x == "**":
    print(num1 ** num2)