from functools import lru_cache
import itertools
from typing import List, Literal, Tuple
import time

def read_file(file_name: str) -> Tuple[List[int]]:
    with open(file_name, mode="r") as f:
        list1 = []
        list2 = []
        for line in f.readlines():
            elements = line.split("   ")
            list1.append(int(elements[0]))
            list2.append(int(elements[1]))

    return list1, list2

@lru_cache
def calculate_distance(el1: int, el2: int):
    return abs(el1 - el2)

def how_many_times_in_list(num: int, lst: List[int]):
    return sum([1 if el == num else 0 for el in lst])

def first_task() -> int:
    input_file = "./data/day_1_input.txt"
    list1, list2 = read_file(input_file)
    # sort both lists from smallest to largest
    res = 0
    for el1, el2 in zip(sorted(list1), sorted(list2)):
        res += calculate_distance(el1, el2)
    return res

def second_task() -> int:
    input_file = "./data/day_1_input.txt"
    list1, list2 = read_file(input_file)
    # sort both lists from smallest to largest
    res = 0
    for el in list1:
        res += el * how_many_times_in_list(el, list2)
    return res

if __name__ == "__main__":
    time1 = 0
    time2 = 0
    t = time.time()
    res1 = first_task()
    time1 = time.time() - t
    t = time.time()
    res2 = second_task()
    time2 = time.time() - t
    print(f"The answer for first task is: {res1}. Time to calculate: {time1}s")
    print(f"The answer for second task is: {res2}. Time to calculate: {time2}s")