# WAP in Python to calculate x y by writing a function (say POWER) for it.

def power(x,y):
    result = 1
    for i in range(1, y+1):
        result  = result * x
    return result

onee = int(input ("Enter your first number: "))
twoo = int(input ("Enter your second number: "))

print(power(onee,twoo))
