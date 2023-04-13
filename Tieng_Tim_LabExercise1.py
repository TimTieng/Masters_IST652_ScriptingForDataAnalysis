# Course: IST-652 Scripting For Data Analysis
# Student: Tim Tieng
# Lab Number: 1
# Due Date: April 14, 2023

# Lab 1 Prompt:
# Write a program to print the cube of all numbers from 1 to 6. A cube of a number is x3 (x * x * x).
# Use a loop (either a for or while loop) to go through the numbers and print out the cube of each number.

# Brute Force
def cubedValues():
    for i in range(7):
        print(i ** 3)

cubedValues()
print("DONE")

# Refactored Solution
def cubedValues2():
    cubedList = []
    for i in range(7):
        cubedList.append(i ** 3)
    print(cubedList)
    return cubedList

cubedValues2()
print("DONE")