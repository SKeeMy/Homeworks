def value(filepath):
    with open(filepath, "r") as file1:
        for line in file1.readlines():
            res = tuple(map(int, line.split(' ')))
            max_tup = max(res)
            min_tup = min(res)
            result = [min_tup, max_tup]
            return result
