def solution(sequence):
    delete = 0
    while len(sequence) >= 4:
        if len(set(sequence[:3])) == 3 and min(sequence[:3]) == sequence[:3][0]:
            del sequence[0]
        elif len(set(sequence[:3])) == 2 and min(sequence[:3]) == sequence[:3][0] and delete == 0:
            delete += 1
            del sequence[0]
        else:
            return False
    return bool(len(set(sequence)) >= 1 and delete == 0 and min(sequence) == sequence[0])


assert solution([1, 1]) is True
assert solution([1]) is True
assert solution([1, 2]) is True
assert solution([1, 3, 2]) is True
assert solution([1, 1, 2]) is True
assert solution([1, 1, 1, 2]) is False
assert solution([1, 2, 3]) is True
assert solution([1, 2, 1, 2]) is False
assert solution([1, 3, 2, 1]) is False
assert solution([1, 2, 3, 4, 5, 3, 5, 6]) is False
assert solution([40, 50, 60, 10, 20, 30]) is False
