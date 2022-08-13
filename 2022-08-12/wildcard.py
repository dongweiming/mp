def wildcard(data):
    match data:
        case [_, _]:
            print('Some pair')


def sequence2(collection):
    match collection:
        case ["a", *_, "z"]:
            print('matches any sequence of length two or more that starts with "a" and ends with "z".')
        case (_, _, *_):
            print('matches any sequence of length two or more.')
        case [*_]:
            print('matches a sequence of any length.')
