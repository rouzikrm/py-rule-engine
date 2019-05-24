import types


def rule(cls):
    def wrapper():
        condition = None
        next_rule = None
        action = None
        for k, v in cls.__dict__.items():
            if isinstance(v, types.FunctionType) and hasattr(v, 'condition') and v.condition:
                condition = v
            if isinstance(v, types.FunctionType) and hasattr(v, 'next_rule') and v.next_rule:
                next_rule = v
            if isinstance(v, types.FunctionType) and hasattr(v, 'action') and v.action:
                action = v
        if condition:
            cls._condition = condition
        if action:
            cls._action = action
        if next:
            cls._next = next_rule
        return cls

    return wrapper
