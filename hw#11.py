# Положительные аргументы функции
def validate_arguments(func):
    def wrapper(*args):
        for arg in args:
            if arg <= 0:
                raise ValueError('Число отрицательное или равное нулю')
        return f'Число "{func(*args)}" прошло проверку'
    return wrapper


@validate_arguments
def example_function(a, b, c):
    return a + b + c


print(example_function(1, 2, 3))
print(example_function(-1, 2, 3))


# Вернуть число
def validate_result(func):
    def wrapper(*args):
        if not all(isinstance(arg, (int, float)) for arg in args):
            print('Результат функции должен быть числом')
        else:
            print(f'{func(*args)} = {type(func(*args))}')
    return wrapper


@validate_result
def example_function1(a, b):
    return a + b


example_function1(2, 3)
example_function1("2", 3)


# Декоратор типов
def typed(style):
    def dec_arg(func):
        def wrapper(*args):
            new_args = [style(arg) for arg in args]
            return func(*new_args)
        return wrapper
    return dec_arg


@typed(style=str)
def add(a, b):
    return a + b


add("3", 5)
add(5, 5)
add('a', 'b')


@typed(style=int)
def add2(a, b, c):
    return a + b + c


add2(5, 6, 7)


@typed(style=float)
def add3(a, b, c):
    return a + b + c


add3(0.1, 0.2, 0.4)
