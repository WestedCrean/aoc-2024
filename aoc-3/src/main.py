from functools import lru_cache
import itertools
from typing import List, Literal, Tuple
import re

def read_file(file_name: str) -> Tuple[List[int]]:
    with open(file_name, mode="r") as f:
        output = []
        for l in f.readlines():
            output.append(l)
    return "".join(output)



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
    reg = re.compile("mul\(\d+\,\d+\)", flags=re.M)
    out = reg.findall(inp)
    res = 0
    for mulstr in out:
        mulstr: str
        a, b = mulstr.replace("mul(", "").replace(")", "").split(",")
        res += int(a) * int(b)
    return res

def second_task() -> int:
    input_file = "./data/input.txt"
    inp = read_file(input_file)
    reg = re.compile("mul\(\d+\,\d+\)|don't\(\)|do\(\)", flags=re.M)
    out = reg.findall(inp)
    res = 0
    add_result = True
    for mulstr in out:
        mulstr: str
        if "mul" not in mulstr:
            if "don't" in mulstr:
                add_result = False
            else:
                if "do" in mulstr:
                    add_result = True
            continue
        if add_result:
            a, b = mulstr.replace("mul(", "").replace(")", "").split(",")
            res += int(a) * int(b)
    return res

if __name__ == "__main__":
    res1 = first_task()
    print(f"The answer for first task is: {res1}")
    res2 = second_task()
    print(f"The answer for second task is: {res2}")
