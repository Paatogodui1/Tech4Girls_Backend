#!/usr/bin/python3

is_student = True
is_employed = True

if is_student and is_employed:
    print("You are a working student.")
elif is_student and not is_employed:
    print("You are a student.")
elif not is_student and is_employed:
    print("You are employed but not a student.")
else:
    print("You are not a student nor are you emplyed.")

#Asking the user for their name
Age = int(input('What is your age?'))
if Age >= 18:
#Asking if the user has a driver's license
    license =input("Do you have a driver's license? (Y/n):")
#if yes then ' You are allowed to drive will be the output'
if license == 'Y':
    print('You are allowed to drive')
#if no then, 'You need a driver's license to drive' will be the output
elif license == 'n':
    print("You need a driver's license to drive")
#if age is less than 18
elif Age < 18:
    print('You are not old enough to drive')
else:
    print('Not qualified to drive')


