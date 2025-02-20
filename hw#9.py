def subsequence(sequence):
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


assert subsequence([1, 1]) is True
assert subsequence([1]) is True
assert subsequence([1, 2]) is True
assert subsequence([1, 3, 2]) is True
assert subsequence([1, 1, 2]) is True
assert subsequence([1, 1, 1, 2]) is False
assert subsequence([1, 2, 3]) is True
assert subsequence([1, 2, 1, 2]) is False
assert subsequence([1, 3, 2, 1]) is False
assert subsequence([1, 2, 3, 4, 5, 3, 5, 6]) is False
assert subsequence([40, 50, 60, 10, 20, 30]) is False


def number_on_the_opposite(n, f_number):
    if f_number >= n // 2:
        return f_number - n // 2
    else:
        return f_number + n // 2


assert number_on_the_opposite(10, 6) == 1
assert number_on_the_opposite(10, 2) == 7
assert number_on_the_opposite(10, 4) == 9
assert number_on_the_opposite(12, 0) == 6
assert number_on_the_opposite(12, 5) == 11
assert number_on_the_opposite(12, 3) == 9
assert number_on_the_opposite(8, 1) == 5
assert number_on_the_opposite(8, 3) == 7
assert number_on_the_opposite(8, 4) == 0
