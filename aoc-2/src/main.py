from functools import lru_cache
import itertools
from typing import List, Literal, Tuple
import time

def read_file(file_name: str) -> Tuple[List[int]]:
    with open(file_name, mode="r") as f:
        output = []
        for line in f.readlines():
            output.append([int(i) for i in line.split(" ")])
    return output

def safe_or_unsafe_task_1(lst: List) -> int:
    monotonic = None # positive if increasing, negative if decreasing
    prev_el = None

    for el in lst:
        if prev_el is None:
            prev_el = el
            continue
        if monotonic is None:
            if el > prev_el:
                monotonic = 1
            if el < prev_el:
                monotonic = -1
        else:
            if el <= prev_el and monotonic == 1:
                return 0
            if el >= prev_el and monotonic == -1:
                return 0

        diff = abs(el - prev_el)
        if not((diff >= 1) & (diff <= 3)):
            return 0
        prev_el = el
    return 1

def safe_or_unsafe_task_2(lst: List) -> int:
    if safe_or_unsafe_task_1(lst) == 0:
        for i in range(len(lst)):
            # remove ith element
            new_lst = lst.copy()
            new_lst.pop(i)
            if safe_or_unsafe_task_1(new_lst) == 1:
                return 1
        return 0
    return 1

test_cases = [
    ([7, 6, 4, 2, 1], 1),
    ([1, 2, 6, 8, 9], 0),
    ([9, 7, 6, 2, 1], 0),
    ([1, 3, 2, 4, 5], 1),
    ([8, 6, 4, 4, 1], 1),
    ([1, 3, 6, 7, 9], 1),
]

def first_task() -> int:
    input_file = "./data/input.txt"
    inp = read_file(input_file)
    res = 0
    for lst in inp:
        res += safe_or_unsafe_task_1(lst)
    return res

def second_task() -> int:
    input_file = "./data/input.txt"
    inp = read_file(input_file)
    res = 0

    for test_case, test_res in test_cases:
        assert safe_or_unsafe_task_2(test_case) == test_res, f"f({test_case}) != {test_res}"

    for lst in inp:
        res += safe_or_unsafe_task_2(lst)
    return res

if __name__ == "__main__":
    res1 = first_task()
    print(f"The answer for first task is: {res1}")
    res2 = second_task()
    print(f"The answer for second task is: {res2}")
