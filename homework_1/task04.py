def check_sum_of_four(a: list[int], b: list[int], c: list[int], d: list[int]) -> int:
    total = {}
    for i in a:
        for j in b:
            if i+j not in total:
                total[i+j] = 1
            else: 
                total[i+j] += 1
            totalizer = 0
            for i in c:
                for j in  d:
                    if -1 * (i+j) in total:
                        totalizer += total[-1*(i+j)]
    return totalizer