import re
from sympy import symbols, Eq, solve, sympify
import time


def flint(a):
    if a.is_integer():
        return int(a)
    else:
        return round(a, 3)


def space(equation):
    equation = re.sub(r"(\d)([a-zA-Z])", r"\1\2", equation)
    equation = re.sub(r"([+\-*/=])", r" \1 ", equation)

    equation = re.sub(r"\s+", " ", equation)
    equation = re.sub(r"^\s*|\s*$", "", equation)

    return equation


def onevariables_equation(persamaan):

    persamaan = persamaan.replace(" ", "")

    persamaan = re.sub(r"(\d)([a-zA-Z])", r"\1*\2", persamaan)

    persamaan = re.sub(r"(\d)\(", r"\1*(", persamaan)

    return persamaan


def eqv1(equation):

    eq_str = onevariables_equation(equation)

    left1, right1 = eq_str.split("=")

    expresi = left1 + right1

    variabel = sorted(set(re.findall(r"[a-zA-Z]", expresi)))
    syms = symbols(variabel)

    eq = Eq(sympify(left1), sympify(right1))

    solution = solve(eq, syms)

    print(f"Equation: {space(equation)}")
    print(f"Solution: {variabel[0]} = {solution[0]}")


def twovariables_equation(equation):

    equation = equation.replace(" ", "")
    equation = re.sub(r"(\d)([a-zA-Z])", r"\1*\2", equation)

    return equation


def eqv2(equation1, equation2):
    x, y = symbols("x y")

    eq1_str = twovariables_equation(equation1)
    eq2_str = twovariables_equation(equation2)

    left1, right1 = eq1_str.split("=")
    left2, right2 = eq2_str.split("=")

    eq1 = Eq(sympify(left1), sympify(right1))
    eq2 = Eq(sympify(left2), sympify(right2))

    solution = solve((eq1, eq2), (x, y))

    print(f"[{space(equation1)}")
    print(f"[{space(equation2)}")
    print(solution)


def three_variables(equation):

    equation = equation.replace(" ", "")

    equation = re.sub(r"(\d)([a-zA-Z])", r"\1*\2", equation)

    equation = re.sub(r"(\b)([a-zA-Z])(\b)", r"1*\2", equation)

    return equation


def eqv3(eq1, eq2, eq3):

    eq1_str = three_variables(eq1)
    eq2_str = three_variables(eq2)
    eq3_str = three_variables(eq3)

    left1, right1 = eq1_str.split("=")
    left2, right2 = eq2_str.split("=")
    left3, right3 = eq3_str.split("=")

    expre = left1 + right1 + left2 + right2 + left3 + right3

    varibles = sorted(set(re.findall(r"[a-zA-Z]", expre)))
    syms = symbols(varibles)

    eqq1 = Eq(sympify(left1), sympify(right1))
    eqq2 = Eq(sympify(left2), sympify(right2))
    eqq3 = Eq(sympify(left3), sympify(right3))

    print(f"[{space(eq1)}")
    print(f"[{space(eq2)}")
    print(f"[{space(eq3)}")
    solution = solve((eqq1, eqq2, eqq3), syms)

    for a, b in solution.items():
        print(f"{a}: {b}", end=" ")
    print()


def quadric_equation(equation):

    equation = equation.replace(" ", "")

    equation = re.sub(r"(\d+)x2", r"\1*x^2", equation)
    equation = re.sub(r"(\b)x2", r"1*x^2", equation)

    equation = re.sub(r"(\d+)x\b", r"\1*x", equation)

    equation = re.sub(r"(\b)x\b", r"1*x", equation)

    return equation


def qeq(equation):
    try:
        x = symbols("x")
        eq_str = quadric_equation(equation)

        left, right = eq_str.split("=")

        left_expr = sympify(left)
        right_expr = sympify(right)

        eq = Eq(left_expr, right_expr)

        solution = solve(eq, x)

        if len(solution) == 2:
            if solution[0] == solution[1]:
                x1_str = str(solution[0]).replace("sqrt", "√").replace("*I", "i")
                print(f"Equation: {equation}")
                print(f"x1, x2: {x1_str}")
            else:
                x1_str = str(solution[0]).replace("sqrt", "√").replace("*I", "i")
                x2_str = str(solution[1]).replace("sqrt", "√").replace("*I", "i")
                print(f"Equation: {equation}")
                print(f"x1: {x1_str}")
                print(f"x2: {x2_str}")

        elif len(solution) == 1:
            x1_str = str(solution[0]).replace("sqrt", "√").replace("*I", "i")
            print(f"Equation: {space(equation)}")
            print(f"x1, x2: {x1_str}")
        else:
            print(f"Equation: {equation}")
            print("No real solutions")

        return solution

    except Exception as e:
        print(f"Error: {e}")
        return None


def menu():
    while True:
        print("Welcome to E - Q - U - A - T - I - O - N - S")

        pilih = {
            "1": "Linear Equations",
            "2": "Quadratic Equations",
            "3": "Inequalities Equations (COMING)",
            "4": "Inequalities Quadratic Equations (COMING)",
            "5": "Exit",
        }

        for no, ber in pilih.items():
            print(f"{no}: {ber}")

        try:
            user = input("You: ").lower()
        except ValueError:
            print("Your choice only between 1 and 2")

        if user in ["5", "exit"]:
            print("Exiting the program.")
            break

        if user in ["1", "linear", "linear equations"]:
            linear_equation()

        if user in ["2", "quadric", "quadrix equations"]:
            quadric()


def linear_equation():
    while True:
        pilih = {
            "1": "One Variable",
            "2": "Two Variables",
            "3": "Three Variables",
            "4": "Menu",
        }

        for no, ber in pilih.items():
            print(f"{no}: {ber}")
        print()

        user = input("You: ").lower()

        if user in ["1", "one", "one variable"]:
            while True:
                print("1. Back")
                print()
                print("ax + b = c")
                print()

                eq1 = input("You: ")

                if eq1 in ["1"]:
                    break

                print()
                print("-" * 15)
                try:
                    eqv1(eq1)
                except ValueError:
                    print("Invalid Input, Try Again!")
                    continue
                print("-" * 15)
                print()

        elif user in ["2", "two", "two variables"]:
            while True:
                print("Press(b) to back")
                print()
                print("ax + by = c")
                print("ax - by = c")
                print()

                eq1 = input("You: ")

                if eq1 in ["1"]:
                    break

                print(f"Equation 1: {eq1}")
                eq2 = input("You: ")
                print(f"Equation 2: {eq2}")

                print()
                print("-" * 15)
                try:
                    eqv2(eq1, eq2)
                except ValueError:
                    print("Invalid Input, Try Again!")
                    continue
                print("-" * 15)
                print()

        elif user in ["3", "three", "three variables"]:
            while True:
                print("1.Back")
                print()
                print("ax + by - cz = d")
                print("ax - by + cz = d")
                print("ax - by + cz = d")
                print()

                eq1 = input("You: ")

                if eq1 in ["1"]:
                    break

                print(f"Equation 1: {space(eq1)}")
                eq2 = input("You: ")
                print(f"Equation 2: {space(eq2)}")
                eq3 = input("You: ")
                print(f"Equation 3: {space(eq3)}")

                print()
                print("-" * 15)
                try:
                    eqv3(eq1, eq2, eq3)
                except ValueError:
                    print("Invalid Input, Try Again!")
                    continue
                print("-" * 15)
                print()

        elif user in ["4", "menu"]:
            menu()


def quadric():
    while True:
        print("1. Back")
        print()
        print("ax2 + bx + c = d")
        print()

        eq1 = input("You: ")

        if eq1 in ["1"]:
            break

        print()
        print("-" * 15)
        try:
            qeq(eq1)
        except ValueError:
            print("Invalid Input, Try Again!")
            continue
        print("-" * 15)
        print()


menu()
