# WAP in Python to calculate GCD/HCF of two numbers by using an iterative function for
# GCD.

def gcd(a, b):
  while b:
    a, b = b, a % b
  return a

onee = int(input ("Enter your first number: "))
twoo = int(input ("Enter your second number: "))

result = gcd(onee , twoo)
print("The GCD of ",onee," and ",twoo," is" , result)
