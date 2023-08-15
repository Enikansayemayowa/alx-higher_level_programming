#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    option = {"+": add, "-": sub, "*": mul, "/": div}

    if sys.argv[2] not in option:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operator = sys.argv[2]
    if operator == "/":
        if b == 0:
            print("Error: Cannot divide by zero")
            sys.exit(1)
    result = option[operator](a, b)
    print("{} {} {} = {}".format(a, operator, b, result))
