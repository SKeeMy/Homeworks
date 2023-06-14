from typing import Any


def find_occurrences(tree: dict, element: Any) -> int:
    count = 0
    if isinstance(tree, list) or isinstance(tree, tuple):
        for i in tree:
            count += find_occurrences(i, element)
    elif isinstance(tree, set):
        for i in tree:
            count += find_occurrences(i, element)
    elif isinstance(tree, dict):
        for key, val in tree.items():
            if key == element:
                count += 1
            count += find_occurrences(val, element)
    else:
        if tree == element:
            count += 1
    return count


if __name__ == '__main__':
    print(find_occurrences(example_tree, "RED"))