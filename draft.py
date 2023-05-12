from tkinter import *
from tkinter import ttk

class Calculator:
    
    def __init__(self, app_interface):
        self.app_interface = app_interface

    def calculate(self):
        operation = self.app_interface.operation_combo.get()
        num1 = float(self.app_interface.num1_entry.get())
        num2 = float(self.app_interface.num2_entry.get())           
        
        try:
            if operation == "Addition":
                result = num1 + num2
            elif operation == "Subtraction":
                result = num1 - num2
            elif operation == "Multiplication":
                result = num1 * num2
            elif operation == "Division":
                if num2 == 0:
                    raise ZeroDivisionError
                result = num1 / num2
            else:
                raise ValueError

            self.app_interface.result_label.config(text=f"Result: {result}")

        except ValueError:
            self.app_interface.result_label.config(text="Invalid input. Please enter valid numbers and operation.")
        except ZeroDivisionError:
            self.app_interface.result_label.config(text="Division by zero is not allowed.")


class AppInterface:
    def __init__(self):
        self.root = Tk()
        self.root.title("Simple App Calculator")
        
        # Create an instance of the Calculator class
        self.calculator = Calculator(self)
        
        # Title Label
        self.title_label = Label(self.root, text="Simple Calculator", font=("Pacifico", 24), bg="white", fg="black")
        self.title_label.pack(pady=20)

        # First Number Entry
        self.num1_label = Label(self.root, text="Enter the first number:", font=("Arimo", 12), bg="white", fg="black")
        self.num1_label.pack()
        self.num1_entry = Entry(self.root, font=("Arimo", 12))
        self.num1_entry.pack(pady=10)

        # Second Number Entry
        self.num2_label = Label(self.root, text="Enter the second number:", font=("Arimo", 12), bg="white", fg="black")
        self.num2_label.pack()
        self.num2_entry = Entry(self.root, font=("Arimo", 12))
        self.num2_entry.pack(pady=10)

        # Operation Combo Box
        self.operation_label = Label(self.root, text="Select the operation to perform: ", font=("Arimo", 12), bg="white", fg="black")
        self.operation_label.pack()
        self.operation_combo = ttk.Combobox(self.root, values=["Addition", "Subtraction", "Multiplication", "Division"], font=("Arimo", 12))
        self.operation_combo.pack(pady=10)

        # Calculate Button
        self.calculate_button = Button(self.root, text="Calculate", font=("Arimo", 12), bg="#4CAF50", fg="white", command=self.calculate)
        self.calculate_button.pack(pady=20)

        # Result Label
        self.result_label = Label(self.root, text="", font=("Hind", 16), bg="white", fg="black")
        self.result_label.pack()

        # Try Again Button
        self.try_button = Button(self.root, text="Try Again", font=("Arimo", 12), bg="#1589FF", fg="white", command=self.try_again)
        self.try_button.pack(pady=20)

        # Exit Button
        self.exit_button = Button(self.root, text="Exit", font=("Arimo", 12), bg="#f44336", fg="white", command=self.on_exit)

        
        self.root.mainloop()

AppInterface()