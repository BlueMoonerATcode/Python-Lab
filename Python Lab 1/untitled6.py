# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 10:20:30 2024

@author: Blue Mooner
"""

marks = int(input("Enter the total marks secured by the student: "))

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B+"
elif marks >= 60:
    grade = "B"
elif marks >= 50:
    grade = "C"
else:
    grade = "F"

print("The grade of the student is:", grade)