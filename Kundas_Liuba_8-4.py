from functools import wraps

def val_checker(l_func):
    def _val_checker(func):

        @wraps(func)
        def wrapper(*args):
            num_list = [el for el in args]  # распаковывает все элементы: кортежи...словари
            n = [f"{func.__name__}({el}: {type(el)})" for el in num_list]
            if func(*n):#l_func
                raise ValueError(f"wrong mean: {l_func}")#работает неправильно
            else:
                print(*func(*args), sep=",\n")

        return wrapper
    return _val_checker

@val_checker(lambda x: x>0)
def calc_cube(*x):
    num_list = [el for el in x if isinstance(el, int) or isinstance(el, float)]
    return [i ** 3 for i in num_list]

try:
    b = calc_cube(7, 8, "f")
except (ValueError, TypeError) as err:
    print(err)


