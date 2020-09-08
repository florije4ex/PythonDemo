# @File    : 9_2_keep_method_meta_info
# @Description:
# @Author  : yangbaihua
# @Department:研发部-测试一组
# @Time    : 2020/9/2 9:35
import time
from functools import wraps


def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result

    return wrapper


@timethis
def countdown(n):
    while n > 0:
        n -= 1

if __name__ == '__main__':
    countdown(1000)
    print(countdown.__name__)
    print(countdown.__doc__)
    print(countdown.__annotations__)