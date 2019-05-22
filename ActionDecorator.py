def action(func):

    def wrapper(*args, **kwargs):

       return func(*args, **kwargs)

    wrapper.action = True
    return wrapper