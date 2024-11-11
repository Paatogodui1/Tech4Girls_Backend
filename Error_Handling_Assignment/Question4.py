#List Index Access
items = ["apple", "banana", "cherry"]
#Asking the user to enter the index of an item in the list.
try:
   index = int(input("Enter the index of the item you want to access: "))
   print("You selected:", items[index])
except IndexError:
   print('Index is out of bounds.')
   

