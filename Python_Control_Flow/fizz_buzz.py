#!/usr/bin/python3
#For loop through number 1 tp 50
for number in range(1, 51):
#if number is divisible by both 3 and 5
 if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
#if number is divisble by 3
 elif number % 3 == 0:
    print("Fizz")
#if number is divisible by 5
 elif number % 5 == 0:
    print("Buzz")
 else:
    print(number)