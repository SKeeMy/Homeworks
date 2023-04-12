from typing import List, Any

def combinations(*args: List[Any]) -> List[List]:
    if not args:
        return [[]]
    else:
        combs = []
        for item in args[0]:
            for sub_comb in combinations(*args[1:]):
                combs.append([item] + sub_comb)
        return combs