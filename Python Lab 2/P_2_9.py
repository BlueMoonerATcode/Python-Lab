# Write a program to create a set of user-defined functions to perform basic mathematical
# operations (addition, subtraction, multiplication, and division) and explore different ways
# of passing parameters to functions.


def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  if y == 0:
    return 
  else:
    return x / y


onee = int(input ("Enter your first number: "))
twoo = int(input ("Enter your second number: "))

print("Your 2 Numbers are: ",onee, "and" ,twoo)
print("Your addition 2 Numbers are: ", add(onee,twoo))
print("Your subtraction of 2 Numbers are: ", subtract(onee,twoo))
print("Your multiplication of 2 Numbers are: ", multiply(onee,twoo))
print("Your division of 2 Numbers are: ", divide(onee,twoo))

