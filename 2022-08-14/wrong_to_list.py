def is_str(obj: object) -> bool:
    return isinstance(obj, str)


def to_list(obj: object) -> list[str]:
    if is_str(obj):
        return list(obj)
    return []
