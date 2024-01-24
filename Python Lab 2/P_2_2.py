# WAP in Python to find the factorial of a number n by using a suitable user defined
# function (say fact) for it.


# check if the number is negative, positive or zero
def factoriall(num):
    factorial = 1
    if num < 0:
     print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
     print("The factorial of 0 is 1")
    else:
     for i in range(1,num + 1):
       factorial = factorial*i
     print("The factorial of",num,"is",factorial)


num = int(input("Enter a number: "))
factoriall(num)   #Calling of function
