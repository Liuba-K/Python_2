
def type_logger(func):
    print("hi")
    def wrapper(*param):
        result_list = [i for i in (*param)]
        return result_list
    return wrapper

@type_logger
def cal_cube(x):
    return x ** 3

a = cal_cube(2, 8)