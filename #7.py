import string


def string_len(inp_string: str, ind: int) -> str:
    return inp_string[:ind] + inp_string[:ind-1][::-1]


print(string_len(string.ascii_lowercase, 4))
