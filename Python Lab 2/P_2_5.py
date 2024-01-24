# WAP in Python to swap the values of two variables by using a suitable user defined
# function (say SWAP) for it.

def swap(a, b):
  temp = a
  a = b
  b = temp
  return a,b

onee = int(input ("Enter your first number: "))
twoo = int(input ("Enter your second number: "))

print("Before swap: x = " , onee, "y = ", twoo )
onee,twoo = swap(onee, twoo)
print("After swap:  x = " , onee, "y = ", twoo )


