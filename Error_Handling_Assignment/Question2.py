#Dictionary Lookup

data = {"name": "Alice", "age": 25, "country": "Wonderland"} 
#Asking the user to enter the any key in data.
key = input("Enter the key you want to look up: ") 
try: 
    print("Value: ", data[key]) 
#Printing out error if user enters a key not in data.
except KeyError: 
    print("KeyError: The key you entered is not in the dictionary.")