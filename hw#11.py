#Положительные аргументы функции
def validate_arguments(func):
    def wrapper(*args):
        for arg in args:
            if arg <= 0:
                raise ValueError('Число отрицательное или равное нулю')
        return f'Число "{func(*args)}" прошло проверку'
    return wrapper


#Вернуть число
def validate_result(func):
    def wrapper(*args):
        if not isinstance(func(*args), (int, float)):
            print('Результат функции должен быть числом')
        return f'{func(*args)} = {type(func(*args))}'
    return wrapper


#Декоратор типов
def typed(style):
    def dec_arg(func):
        def wrapper(*args):
            new_args = [style(arg) for arg in args]
            return func(*new_args)
        return wrapper
    return dec_arg
