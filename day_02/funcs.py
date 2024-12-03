from typing import List

def construct_reports(input_str: str) -> List[List[int]]:
    reports = []
    for line in input_str.splitlines():
        levels = [int(x) for x in line.split(' ')]
        reports.append(levels)
    return reports

def is_safe(report: List[int]) -> bool:
    def sign(x):
        return (x > 0) - (x < 0)
    signedness = 0
    for i, j in zip(report[:-1], report[1:]):
        diff = i - j
        if signedness == 0:
            signedness = sign(diff)
        elif signedness != sign(diff):
            return False
        if abs(diff) == 0 or abs(diff) > 3:
            return False
    return True

def is_safe_with_problem_dampener(report: List[int]) -> bool:
    if is_safe(report):
        return True
    variants = [report[:i] + report[i+1:] for i in range(len(report))]
    for vrnt in variants:
        if is_safe(vrnt):
            return True
    return False
