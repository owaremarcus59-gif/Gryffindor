'''The assignment 1: rewrite the  parity function , use try except and try to catch error to keep the app flow working even when there are errors'''
def parity():
    try:
        number = int(input("Enter a number: "))   # Try converting input to integer
        
        if number % 2 == 0:
            return "Even"
        else:
            return "Odd"
    
    except ValueError:
        return "Invalid input: Please enter a valid integer."
    
    except TypeError:
        return "Invalid type: Input must be a number."
output = parity()
print(output)
def parity():
    try:
        num= int(input("Enter a number: "))
        return "Even" if num % 2 == 0 else "Odd"
    
    except Exception as e:
        print(f"Error: {e}")
        return None
consult = parity()
print(consult)    