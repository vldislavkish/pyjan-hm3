def conversion_plus_one(lst):
    lst = lst[::-1]
    while 9 in lst:
        for i, v in enumerate(lst):
            if v in (9, 10):
                lst[i] = 0
                if i + 1 < len(lst):
                    lst[i + 1] += 1

    if sum(lst) == 0:
        lst.append(1)
    return lst[::-1]


print(conversion_plus_one([1, 1, 9, 9]))
