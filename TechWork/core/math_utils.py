def square(x):
    if isinstance(x, (int, float)):
        return x * x
    elif isinstance(x, list):
        return [i * i for i in x]
    else:
        raise TypeError("Input must be a number or list of numbers")