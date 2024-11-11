#Division Calculator

def Division_Calculator(): 
    try: 
        numerator = int(input("Enter the numerator: ")) 
        denominator = int(input("Enter the denominator: "))
# Checking if the denominator is zero  
        if denominator == 0: 
            print("Error; division by zero is not possible. Please enter a non-zero integer.") 
        else: 
          result = numerator / denominator 
          print("The result is: ", result) 
    except ValueError: 
        print("Invalid input. Please enter valid integers.") 

Division_Calculator()