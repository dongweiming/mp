from typing import Literal

def accepts_only_four(x: Literal[4]) -> None:
    pass

accepts_only_four(4)   # OK
accepts_only_four(19)  # Rejected
accepts_only_four(2 + 2)  # Rejected

from typing import LiteralString


def get_user_sql(user_id):
    return f"SELECT * FROM users WHERE user_id = '{user_id}'"


get_user_sql("Bob")
get_user_sql(input())
