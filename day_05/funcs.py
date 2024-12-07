from typing import Dict, List, Tuple
import re

def get_number_ordering(rules: str) -> Dict[str, List[str]]:
    graph = {}
    for match in re.finditer(r"([1-9][0-9])\|([1-9][0-9])", rules):
        parent, child = match[1], match[2]
        if parent in graph:
            graph[parent].add(child)
        else:
            graph[parent] = {child}
    return graph

def group_updates(updates: str, ordering: Dict[str, List[str]]) -> Tuple[List[List[str]], List[List[str]]]:
    valid = []
    invalid = []
    regex = re.compile(r"([1-9][0-9]),(?=([1-9][0-9]))")
    for line in updates.splitlines():
        matches = regex.findall(line)
        if matches:
            entry = []
            is_valid = True
            for parent, child in matches:
                entry.append(parent)
                if is_valid and (parent not in ordering or child not in ordering[parent]):
                    is_valid = False
            entry.append(child)
            if (is_valid):
                valid.append(entry)
            else:
                invalid.append(entry)
    return valid, invalid
