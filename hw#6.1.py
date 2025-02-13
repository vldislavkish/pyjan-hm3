import datetime


def moto_time(inp_m):
    if not 0 < inp_m < 1440:
        raise ValueError
    inp_h = 0
    while inp_m >= 60:
        inp_m -= 60
        inp_h += 1
    ans_m = list(map(int, [_ for _ in str(inp_m)]))
    ans_h = list(map(int, [_ for _ in str(inp_h)]))
    print(datetime.time(hour= inp_h, minute=inp_m), sum(ans_h + ans_m))


moto_time(1439)
