import types
def rule(cls):
    def  wrapper():
        condition = None
        next = None
        action = None
        for k,v in cls.__dict__.items():
            if type(v) == types.FunctionType and hasattr(v,'condition') and v.condition:
                condition = v
            if type(v) == types.FunctionType and hasattr(v,'next') and v.next:
                next = v
            if type(v) == types.FunctionType and hasattr(v,'action') and v.action:
                action = v
        if condition:
            cls._condition = condition
        if action:
            cls._action = action
        if next:
            cls._next = next
        return cls
    return wrapper