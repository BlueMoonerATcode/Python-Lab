# WAP in Python to test whether a number n is a palindrome number or not.

def palindrome():
    num = int(input("Enter the number:"))
    temp = num
    rev = 0
    while(num > 0):
        dig = num % 10
        rev = rev * 10 + dig
        num=num//10
    
    if temp == rev:
        print("The number is a Palindrome!")
    
    else:
        print("The number is not a Palindrome!!")

palindrome()
