def show_type(obj: int | str):
    if isinstance(obj, int):
        return 'int'
    return 'str'
