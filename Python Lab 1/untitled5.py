# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 10:20:22 2024

@author: Blue Mooner
"""

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")