# main.py
from calculator import add, subtract, multiply, divide, mod


def repl():
    print("Simple calculator (type 'q' to quit)")
    while True:
        expr = input("Enter: <op> <num1> <num2> (e.g. add 2 3): ")
        if not expr or expr.strip().lower() == 'q':
            break
        parts = expr.split()
        if len(parts) != 3:
            print("Invalid input. Example: add 2 3")
            continue
        op, a_str, b_str = parts
        try:
            a = float(a_str)
            b = float(b_str)
        except ValueError:
            print("Numbers invalid")
            continue
        try:
            if op == 'add':
                print(add(a, b))
            elif op == 'sub' or op == 'subtract':
                print(subtract(a, b))
            elif op == 'mul' or op == 'multiply':
                print(multiply(a, b))
            elif op == 'div' or op == 'divide':
                print(divide(a, b))
            elif op == 'mod':
                print(mod(a, b))
            else:
                print('Unknown op: ' + op)
        except Exception as e:
            print('Error:', e)


if __name__ == '__main__':
    repl()



