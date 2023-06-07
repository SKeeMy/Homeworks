from heapq import merge
def merge_sorted_files(file_list: List[Union[Path, str], ...]) -> Iterator:
    iterators = []
    for file in file_list:
        with open(file) as f:
            iterators.append(map(int, f.readlines()))
    return merge(*iterators)