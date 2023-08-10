#!/usr/bin/python3
if __name__ == "__main__":
    a = 10
    b = 5
    import calculator_1 as data
    print("{} + {} = {}".format(a, b, data.add(a, b)))
    print("{} - {} = {}".format(a, b, data.sub(a, b)))
    print("{} * {} = {}".format(a, b, data.mul(a, b)))
    print("{} / {} = {}".format(a, b, data.div(a, b)))
