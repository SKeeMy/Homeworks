from functools import reduce


def is_armstrong_number(num: int) -> bool:
    if not isinstance(num, int):
        raise TypeError("Input must be an integer")
    if num < 0:
        return False
    digits = [int(d) for d in str(num)]
    num_digits = len(digits)
    sum_of_cubes = reduce(lambda x, y: x + y,
                          (d ** num_digits for d in digits))
    return sum_of_cubes == num
