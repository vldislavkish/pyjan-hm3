import datetime


def moto_time(inp_m: int) -> None:
    if not 0 < inp_m < 1440:
        raise ValueError
    inp_h = 0
    while inp_m >= 60:
        inp_m -= 60
        inp_h += 1
    ans_m = list(map(int, list(str(inp_m))))
    ans_h = list(map(int, list(str(inp_h))))
    print(datetime.time(hour=inp_h, minute=inp_m), sum(ans_h + ans_m))


def level_up(experience: int, threshold: int, reward: int) -> None:
    print(experience + reward >= threshold)


def time_converter(time: str) -> None:
    hour: int = int(time.split(':')[0])
    minute: str = time.split(':')[1]
    if 0 < hour < 12:
        print(f'{hour}:{minute} a.m.')
    elif hour == 12:
        print(f'{hour}:{minute} p.m.')
    elif hour == 0:
        hour += 12
        print(f'{hour}:{minute} a.m.')
    else:
        hour -= 12
        print(f'{hour}:{minute} p.m.')
