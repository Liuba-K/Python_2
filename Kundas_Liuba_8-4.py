from functools import wraps

def val_checker(lambda_func):
    def _val_checker(func):

        @wraps(func)
        def wrapper(number):
            if not lambda_func(number):
                raise ValueError(f"wrong mean: {number}")
            else:
                print(func(number), sep=",\n")

        return wrapper
    return _val_checker

@val_checker(lambda x: x>0)
def calc_cube(x):
    return [x ** 3]

number_1 = calc_cube(5)
number_2 = calc_cube(-5)