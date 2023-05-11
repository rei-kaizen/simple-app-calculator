
def calculator():
    # ask the user to choose one of four math operations:
    user_choice_operation = input("Choose one of the operations (Addition, Subtraction, Multiplication, and Multiplication): ")  
    ## Addition, Subtraction, Multiplication, and Multiplication
    # ask the user to enter two numbers
    user_num1 = float(input("Enter the 1st number: "))
    user_num2 = float(input("Enter the 2nd number: "))
    # display the result
    if user_choice_operation == "Addition":
        print(user_num1 + user_num2)
    elif user_choice_operation == "Subtraction":
        print(user_num1 - user_num2)
    elif user_choice_operation == "Multiplication":
        print(user_num1 * user_num2)
    elif user_choice_operation == "Division":
        print(user_num1 / user_num2)
    else:
        print("Invalid Operation")

calculator()
    # use loop to ask if the user wants to try again or not.
    ## If yes, then perform the operation again.
    ## if no, Display “Thank you!”\
    # then the program will exit
    #Use Python Functions and appropriate Exceptions to capture errors during runtime.