
def calculator():
    # ask the user to choose one of four math operations:
    user_choice_operation = input("Choose one of the operations (Addition, Subtraction, Multiplication, and Multiplication): ")  
    ## Addition, Subtraction, Multiplication, and Multiplication
    # ask the user to enter two numbers
    user_num1 = input("Enter the 1st number: ")
    user_num2 = input("Enter the 2nd number: ")
    
    
    # use Python Functions and appropriate Exceptions to capture errors during runtime.
    try:
        if (user_num1.isnumeric() and user_num2.isnumeric()):
            user_num1 = float(user_num1)
            user_num2 = float(user_num2)  
            # display the result
            if user_choice_operation == "Addition":
                print(user_num1 + user_num2)
            elif user_choice_operation == "Subtraction":
                print(user_num1 - user_num2)
            elif user_choice_operation == "Multiplication":
                print(user_num1 * user_num2)
            elif user_choice_operation == "Division":
                if user_num2 == 0:
                    raise ZeroDivisionError("Division by zero is undefined :|")
                print(user_num1 / user_num2)
            else:
                raise Exception("Add, Subtract, Multiplication and Division operations only :(")
        else:
            raise ValueError("Please enter a valid numbers :)")
    
    except ValueError as raised :
        print(raised)
    except ZeroDivisionError as raised:
        print(raised)
    except Exception as raised:
        print(raised)

    finally:
        print("===" * 3)
            
        # use loop to ask if the user wants to try again or not.
        while True:
            user_attempt = input("Do you want to try again or not? (yes/no): ")
            ## If yes, then perform the operation again.
            if user_attempt == "yes":
                calculator()
            ## if no, Display “Thank you!”
            else:
                print("Thank you!")
            
            break
                
            # then the program will exit
                    
calculator()