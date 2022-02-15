from datetime import datetime


def time_func(func, repeat=1):
    def wrapper(*args, **kwargs):
        accum = datetime.now() - datetime.now()
        for _ in range(repeat):
            start = datetime.now()
            result = func(*args, **kwargs)
            accum += datetime.now() - start
        print(f'Среднее время выполнения функции {func.__name__}: {accum / repeat}, количество повторений: {repeat}')
        return result

    return wrapper
