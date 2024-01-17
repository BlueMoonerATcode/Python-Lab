# Calculator-Lite

#Introduction to User
print("******Calculator-Lite******")

#Taking Inputs:
First = input("Enter your First Number: ")
Second = input("Enter your Second Number: ")
operator = input("Enter your Operator (+,-,*,/,%): ")

#Typecasting to Integer for Operations:
First = int(First)
Second = int(Second)

#Using if,elif and else for determining operations:
if operator == "+":
    print(First+Second)
elif operator == "-":
    print(First-Second)
elif operator == "*":
    print(First*Second)
elif operator == "/":
    print(First/Second)
elif operator == "%":
    print(First%Second)
else:
    print("Invalid Operation")






