import logging
from collections.abc import Callable
from typing import TypeVar, ParamSpec, Concatenate

logging.basicConfig(level=logging.NOTSET)
R = TypeVar('R')
P = ParamSpec('P')


def with_logger(func: Callable[Concatenate[logging.Logger, P], R]) -> Callable[P, R]:
    def inner(*args: P.args, **kwargs: P.kwargs) -> R:
        logger = logging.getLogger(func.__name__)
        return func(logger, *args, **kwargs)
    return inner


@with_logger
def join(logger: logging.Logger, items: list[str]):
    logger.info('Info')
    return ','.join(items)


print(join(['1', '2']))
print(join([1, 2]))
