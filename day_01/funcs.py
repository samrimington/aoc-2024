from typing import Dict, List, Tuple

def construct_pair_of_lists(input_str: str) -> Tuple[List[int], List[int]]:
    left_list = []
    right_list = []
    for line in input_str.splitlines():
        if not line:
            continue
        first_num, second_num = line.split('   ')
        left_list.append(int(first_num))
        right_list.append(int(second_num))
    return left_list, right_list

def calc_distance_between_lists(left: List[int], right: List[int]) -> List[int]:
    assert len(left) == len(right)
    distances = []
    for i in range(len(left)):
        difference = abs(left[i] - right[i])
        distances.append(difference)
    return distances

def calc_similarity_scores(num_list: List[int], num_frequency: Dict[int, int]):
    scores = []
    for n in num_list:
        scr = n * num_frequency.get(n, 0)
        scores.append(scr)
    return scores
