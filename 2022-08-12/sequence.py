def sequence(collection):
    match collection:
        case 1, [x, *others]:
            print(f"Got 1 and a nested sequence: {x=}, {others=}")
        case (1, x):
            print(f"Got 1 and {x}")
        case [x, y, z]:
            print(f"{x=}, {y=}, {z=}")


def sequence2(collection):
    match collection:
        case 1, [x, *others]:
            print(f"Got 1 and a nested sequence: {x=}, {others=}")
        case 1, x:
            print(f"Got 1 and {x}")
        case x, y, z:
            print(f"{x=}, {y=}, {z=}")
