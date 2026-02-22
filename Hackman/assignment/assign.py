"""
create a custom function that will check for parity.
to determine if a number is even or odd.
"""
def parity():
    number = 2
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

parity()        




# assignment 2: create a function that will check for parity.

def main():
    parity = parity_function("put in number: \n")
    print(parity)



def parity_function(answer):
    
    while True:
        try:
            number = int(input(answer))
            break
        except (TypeError, ValueError) as e:
            print(e, " __ Please number ")
            continue

    if number % 4 == 0:
        return "number is Even number"
    
    else:
        return "Number is Odd number"
    


if __name__ == "__main__":
    main()
