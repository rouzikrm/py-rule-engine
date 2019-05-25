def fact_message(validated_by=None):
    def wrapper(cls):
        cls._validated_by = validated_by
        return cls

    return wrapper
