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
def maxCapacity(costs: List[int], capacity: List[int], budget: int) -> int:
    n = len(costs)
    prefix_cap = [0]*n
    cost_sorted,cap_sorted = zip(*sorted(zip(costs,capacity)))
    print(cost_sorted,cap_sorted)
    for i in range(n):
        prefix_cap[i] = max(cap_sorted[i], prefix_cap[i-1] if i> 0 else 0)

    res = cap_sorted[0] if cost_sorted[0]< budget else 0
    
    for i in range(1,n):
        if cost_sorted[i]>=budget:
            break
        res = max(res, cap_sorted[i]) 
        # idx = bisect.bisect_right(cost_sorted,budget-cost_sorted[i]-1)-1
        idx = bisect.bisect_right(cost_sorted,budget-cost_sorted[i]-1)-1
        print(i,idx,prefix_cap)
        # if idx>=0 and idx < i:
        idx = min(idx,i-1)
        if idx>=0:
            print(f"i:{i},cost_sorted[i]:{cost_sorted[i]},cost_sorted:{cost_sorted},idx:{idx},prefix:{prefix_cap}")
            # res = max(res, cap_sorted[i]+prefix_cap[cost_sorted[idx]])
            res = max(res, cap_sorted[i]+prefix_cap[idx])
        
    return res
        
@timer
def solve():
    # write your unit tests here
    # print(maxCapacity([4,8,5,3],[1,5,2,7],8))
    # print(maxCapacity([3,5,7,4],[2,4,3,6],7))
    # print(maxCapacity([2,2,3,3,4,4],[1,2,3,4,5,5],6))
    print(maxCapacity([2,2,2],[3,4,5],5))
    return
if __name__ == '__main__':
    solve()