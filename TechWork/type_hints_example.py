from typing import Union

Number = Union[int, float]

def square(x: Number) -> Number:
    return x * x

print(square(5))
print(square(3.5))