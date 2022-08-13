def as_pattern(obj):
    match obj:
        case str() as s:
            print(f'Got str: {s=}')
        case [0, int() as i]:
            print(f'Got int: {i=}')
        case [tuple() as tu]:
            print(f'Got tuple: {tu=}')
        case list() | set() | dict() as iterable:
            print(f'Got iterable: {iterable=}')
