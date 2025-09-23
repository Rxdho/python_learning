import numpy as np
import time



def menu():
    operation = {
        "1" : "Matrix Addition",
        "2" : "Matrix Subtraction",
        "3" : "Matrix Multiplication",
        "0" : "Leave"
    }

    print("-" *5, "MENU", '-' *5)
    for number, lis in operation.items():
        print(f"{number}: {lis}")
    print()

def matrix_input(name=""):
    line = int(input(f"Line {name}: "))
    column = int(input(f"Column {name}: "))
    return line, column

def matrix_create(line, column):
    return np.arange(1, line * column +1).reshape((line, column))

def matrix_valid(line1, column1, line2, column2):
    return line1 == line2 and column1 == column2

def matrix_mulp_valid(column1, line2):
    return column1 == line2

def addition():
    print("-" *5, "ADDITION", '-' *5)
    l1, c1 = matrix_input("Matrix 1")
    matrix1 = matrix_create(l1, c1)
    print("Matrix 1")
    print()
    print(matrix1)
    print()

    l2, c2 = matrix_input("Matrix 2")

    if not matrix_valid(l1, c1, l2, c2):
        print("The Line and Column must be the same!")
        return
    
    matrix2 = matrix_create(l2, c2)
    print("Matrix 2")
    print()
    print(matrix2)
    print()

    print()
    print("-" *5, "ADDITIONING", '-' *5)
    time.sleep(2)
    print()
    total = matrix1 + matrix2
    print("-" *5, "ADDITIONED", '-' *5)
    print()
    print(total)



def subtraction():
    print("-" *5, "SUBTRACTION", '-' *5)
    l1, c1 = matrix_input("Matrix 1")
    matrix1 = matrix_create(l1, c1)
    print("Matrix 1")
    print()
    print(matrix1)
    print()

    l2, c2 = matrix_input("Matrix 2")

    if not matrix_valid(l1, c1, l2, c2):
        print("The Line and Column must be the same!")
        return
    
    matrix2 = matrix_create(l2, c2)
    print("Matrix 2")
    print()
    print(matrix2)
    print()

    print()
    print("-" *5, "SUBTRACTIONING", '-' *5)
    time.sleep(2)
    print()
    total = matrix1 - matrix2
    print("-" *5, "SUBTRACTIONED", '-' *5)
    print()
    print(total)




def multiplication():
    print("-" *5, "MULTIPLICATION", '-' *5)
    l1, c1 = matrix_input("Matrix 1")
    matrix1 = matrix_create(l1, c1)
    print("Matrix 1")
    print()
    print(matrix1)
    print()

    l2, c2 = matrix_input("Matrix 2")

    if not matrix_mulp_valid(c1, l2):
        print("The A Column and B Line must be the same!")
        return
    
    
    
    matrix2 = matrix_create(l2, c2)
    print("Matrix 2")
    print()
    print(matrix2)
    print()

    print()
    print("-" *5, "MULTIPLICATIONING", '-' *5)
    time.sleep(2)
    print()
    total = np.dot(matrix1, matrix2)
    print("-" *5, "MULTIPLICATIONED", '-' *5)
    print()
    print(total)




while True:
    menu()
    choice = input("You: ")

    if choice == '0':
        print("GoodBYE")
        break

    if choice == '1':
        addition()
    elif choice == '2':
        subtraction()
    elif choice == '3':
        multiplication()
    else:
        print("Wrong choice!")


    print("\n" + "=" * 40)
    time.sleep(1)




        

            









    