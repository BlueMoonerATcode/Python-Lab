#Python Basics! 
#          -Aaryan Tiwari


name = input("What is your Name? ")  # Taking input with printing something

# Taking input with printing something with typecasting string to int
age = int(input ("What is your Age? ")) 

# If-Else Condition
if age > 18: 
    isAdult = True
else: 
    isAdult= False

# "else-if" is known as "elif"
    
print("Hey", name , "! Welcome to Python, I heard your age is", age , "& You are an Adult: ",isAdult)

# Finding a letter
hero = "Spider-Man"
print("Your Hero name is: ", hero)
print("Letter M is in position with hero.find: " , hero.find('M'))

# Replacing a letter
print("Replacing Spider-Man with a New Hero with hero.replace: " , hero.replace("Spider-Man","Iron Man")) 

#Arithmetic Operators
print("Normal 5 Divided by 2 (5/2): " , 5/2) #Normal Operation
print("5 Divided by 2 with // to not print Decimal: ", 5//2) #Decimal wont be printed

print("To Print 5 power 2 use 5**2: ", 5**2)

print("As a shortcut: i = i + 2 can also be written as: i+=2") #Same with other operators

#in "and" if both conditions are true, then only true otherwise false
#in "or" if even one condition is true, then true otherwise false


#Range = numbers from 0 to n-1
numbers = range(6)
print("The range using 'range' keyword from 0 to 6 is: " ,numbers, "but 6 is not included")

#While-Loops
i = int(input("You want loop from: "))
j = int(input("You want loop till: "))
print("Running a print loop from", i , "till", j, ":" )
while i <= j:
  print(i)
  i=i+1

#For-Loops
  print("Printing range of 5 using for-loop: ")
for k in range(5):
   print(k) #Printing numbers in Range using for-loop


#List: Collection of items (Complex Data Type) (We know it as Array)
marks = [95,99,90] #Created a list (Any name and any type of data can be added)
print("Marks list is: " , marks)

#printing nth item of list (starting from 0)
print("Number on 2nd position, starting from 0: " ,marks[2]) 
#To count from back use "-1" for last, "-2" for second last etc.

marks.insert(0,92) #Added 92 on 1st position
print("Updated Marks list is: " , marks)
print("Is 92 in Marks list: " , 92 in marks) #Checks if 99 is available in list
print("Length of Marks List is: ", len(marks)) #Gives Length
marks.clear()  #Emptied the List
 
#Break and Continue
newStd = ["Aru","Rishi","Megha","Sabur","Harsh","Shivesh","Anushka","Ojas","Ria"]
print("Printing the new list", newStd, "till Anushka name comes in: ")

for studentt in newStd:
   if studentt == "Anushka":
      break  #Breaks the loop here and then print till "just before the condition"
   print (studentt)

print("Printing the list Excluding the name Ojas:")
for studentt in newStd:
   if studentt == "Ojas":
      continue #Continue the list after condition
   print (studentt)

# "{}" : Set
# "[]" : List
# "()" : Tuple (Optional)
   
age = (21,20,25,50)
print("Ages of random people are: ", age)
print("Index of age 25 (using age.index) is: ", age.index(25))


#Dictionary: Key-Value pairs are stored
grades = {"Physics": 95 , "Chemistry": 98}

#Printing Using Dictionary
print("Printing the marks of Chemistrty (using Dictionary): " ,grades["Chemistry"]) 

grades["Maths"] = 96 #Updation in Dictionary
print("Printing Grades of PCM: " ,grades)


#Functions: In-Built [eg: int(), str()], Module, User-Defined

from math import sqrt #Math Module
print(sqrt(16))

#-> User Defined:

#If assign two=4 then if not mentioned two it will automatically take two = 4
def p_sum(one,two):   
   print(one + two)

p_sum(2,3) #Function Call


#Basics Ends Here!