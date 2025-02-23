def lines_character(text: str) -> str:
    if len(text) / 2 <= text.count('#'):
        return ''
    else:
        text_lst = list(text)
        while text_lst.count('#') > 0:
            ind = text_lst.index('#')
            del text_lst[ind - 1: ind + 1]

        return ''.join(text_lst)


assert lines_character("a#bc#d") == "bd"
assert lines_character("abc#d##c") == "ac"
assert lines_character("abc##d######") == ""
assert lines_character("#######") == ""
assert lines_character("") == ""


def candles(candle_number: int, make_new: int, count=0, left=0) -> int:
    count += candle_number
    left += candle_number
    while left > 0 and candle_number > 0:
        candle_number = int((left - (left % make_new)) / make_new)
        left %= make_new
        count += candle_number
        left += candle_number
    return count


assert candles(5, 2) == 9
assert candles(1, 2) == 1
assert candles(15, 5) == 18
assert candles(12, 2) == 23
assert candles(6, 4) == 7
assert candles(13, 5) == 16
assert candles(2, 3) == 2


def counting_num_let(text: str) -> str:
    new_lst = []
    new_text = list(text)
    for i, v in enumerate(new_text):
        new_lst.append(v)
        count = 1
        for ii, vv in enumerate(new_text[i + 1:]):
            if vv == v:
                count += 1
                del new_text[ii]
                continue
            else:
                break
        if count > 1:
            new_lst[i] += str(count)
    return ''.join(new_lst)


assert counting_num_let("cccbba") == "c3b2a"
assert counting_num_let("abeehhhhhccced") == "abe2h5c3ed"
assert counting_num_let("aaabbceedd") == "a3b2ce2d2"
assert counting_num_let("abcde") == "abcde"
assert counting_num_let("aaabbdefffff") == "a3b2def5"
