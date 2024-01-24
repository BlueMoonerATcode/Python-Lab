# WAP in Python to find out the sum of digits of a number n by using function.

def sum_of_digits(n): 
    sum = 0
    while n: 
        sum = sum + n % 10  # Extract the last digit and add it to the sum
        n //= 10  # Remove the last digit from the number
    return sum

n = int(input ("Enter your number: "))
result = sum_of_digits(n)
print("The sum of digits of" , n , "is", result)
