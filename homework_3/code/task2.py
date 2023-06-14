

import time
import struct
import random
import hashlib
from multiprocessing import Pool


def slow_calculate(value):
    '''Some weird voodoo magic calculations'''
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack('<' + 'B' * len(data), data))


if __name__ == '__main__':
    with Pool() as pool:
        values = range(501)
        results = pool.map(slow_calculate, values)
        total_sum = sum(results)
        print(total_sum)
