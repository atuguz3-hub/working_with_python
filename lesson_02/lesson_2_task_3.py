import math


def square(side):
    area = side * side

    if side != int(side):
        return math.ceil(area)

    return area


print(square(5))
print(square(5.2))