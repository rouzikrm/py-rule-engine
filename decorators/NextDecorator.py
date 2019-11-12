from rule_subtype.Rule import Rule


def next_rule(func):
    def wrapper(*args, **kwargs):
        return Rule().validate(func(*args, **kwargs))

    wrapper.next_rule = True
    return wrapper
