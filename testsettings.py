from typing import List, Dict, Optional, Tuple
import os
import sys
import bisect
import heapq
import functools
import collections
import time

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f'\n[Execution time: {end_time - start_time:.6f} seconds]')
        return result
    return wrapper

# Write your function here


@timer
def solve():
    # write your unit tests here
    return
if __name__ == '__main__':
    solve()