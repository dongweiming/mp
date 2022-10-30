class Duck:
    def quack(self) -> str:
        return "Quack."


def sonorize(duck: Duck) -> None:
    print(duck.quack())


sonorize(Duck())


from typing import Protocol


class Quacker(Protocol):
    def quack(self) -> str:
        ...


class OtherDuck:
    def quack(self) -> str:
        return "QUACK!"


def sonorize2(duck: Quacker) -> None:
    print(duck.quack())


sonorize2(Duck())
sonorize2(OtherDuck())
