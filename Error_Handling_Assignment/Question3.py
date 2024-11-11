#Integer Conversion

def Integer_Conversion(): 
    user_input = input("Enter a number: ") 
    try: 
        converted_number = int(user_input) 
        print("The number you entered is:", converted_number) 
    except ValueError: 
        print("Invalid input. Input is not numeric. Please enter a valid integer.")

# Calling out the function
Integer_Conversion()