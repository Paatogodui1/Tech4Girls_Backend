#!/usr/bin/python3
#Asking user for age
Age = int(input('What is your age?'))

if Age < 18:
    print('You are a minor')
elif 18 <= Age <= 64:
    print('You are an adult')
else:
    print('You are a senior')
