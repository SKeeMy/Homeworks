from typing import List, Tuple

def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    counts = {}
    for el in inp:
        if el not in counts:
            counts[el] = 0
        counts[el] += 1
    major = minor = None
    for el, cnt in counts.items():
        if major is None or cnt > counts[major]:
            major = el
        if minor is None or cnt < counts[minor]:
            minor = el
    return major, minor