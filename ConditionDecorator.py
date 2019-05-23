def condition(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    wrapper.condition = True
    return wrapper
