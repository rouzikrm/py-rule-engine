from Rule import Rule


def next(func):
    def wrapper(*args, **kwargs):
        print("Here SAMA!")
        return Rule().validate_rule(func(*args, **kwargs))

    wrapper.next = True
    return wrapper
