#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1
    import sys
    argv = sys.argv
    num = len(argv)

    if num != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    op = argv[2]
    if op not in('+', '-', '*', '/'):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(argv[1])
    b = int(argv[3])
    if op == '+':
        print("{} + {} = {}".format(a, b, calculator_1.add(a, b)))
    if op == '-':
        print("{} - {} = {}".format(a, b, calculator_1.sub(a, b)))
    if op == '*':
        print("{} * {} = {}".format(a, b, calculator_1.mul(a, b)))
    if op == '/':
        print("{} / {} = {}".format(a, b, calculator_1.div(a, b)))
