#!/usr/bin/python3
if __name__ == "__main__":
    a = 10
    b = 5
    import calculator_1 as data
    result = data.add(a, b)
    print(f"{a} + {b} = {result}")
    result = data.sub(a, b)
    print(f"{a} - {b} = {result}")
    result = data.mul(a, b)
    print(f"{a} * {b} = {result}")
    result = data.div(a, b)
    print(f"{a} / {b} = {result}")
