from typing import List, Tuple
import re

REGEX_1 = r"mul\(([1-9][0-9]{0,2}),([1-9][0-9]{0,2})\)"
REGEX_2 = r"(do(?:n't)?)\(\)|" + REGEX_1

def get_mul_instructions(input_str: str) -> List[Tuple[int, int]]:
    results = []
    for match in re.finditer(REGEX_1, input_str):
        first_digit = int(match.group(1))
        second_digit = int(match.group(2))
        results.append((first_digit, second_digit))
    return results

def get_conditional_mul_instrs(input_str: str) -> List[Tuple[int, int]]:
    results = []
    mul_enabled = True
    for match in re.finditer(REGEX_2, input_str):
        if match.group(1) == "do":
            mul_enabled = True
        elif match.group(1) == "don't":
            mul_enabled = False
        elif mul_enabled:
            first_digit = int(match.group(2))
            second_digit = int(match.group(3))
            results.append((first_digit, second_digit))
    return results
