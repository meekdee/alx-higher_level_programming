#!/usr/bin/python3

if __name__ == "__main__":
    """Print the sum of 1 and 2."""
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    result_add = add(a, b)
    print("{0} + {1} = {2}".format(a, b, result_add))

    result_sub = sub(a, b)
    print("{0} - {1} = {2}".format(a, b, result_sub))

    result_mul = mul(a, b)
    print("{0} * {1} = {2}".format(a, b, result_mul))

    result_div = div(a, b)
    print("{0} / {1} = {2}".format(a, b, result_div))
