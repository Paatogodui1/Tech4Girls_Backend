#Age Validator

#Asking the user to enter their age.
def Age_Validation():
 try:
  age = int(input("Enter your age: "))
  if age < 0:
    print("Age cannot be negative!")
  elif age > 120:
    print("That age is unlikely!")
  else:
    print("Your age is:", age)
 except ValueError:
   print('Invalid input: Your input is non-numeric. Please enter a valid integer.')

Age_Validation()