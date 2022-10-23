'''def get_summary() -> dict[str, int|str|list[str]]:
    return {
        'total': 100,
        'title': 'test',
        'items': ['1', '2']
    }


summary = get_summary()
total = summary['total']
items = summary['items']
print(total / len(items))
'''

from typing import TypedDict


class Summary(TypedDict):
    total: int
    title: str
    items: list[str]



def get_summary() -> Summary:
    return {
        'total': 100,
        'title': 'test',
        'items': ['1', '2']
    }


summary = get_summary()
total = summary['total']
items = summary['items']
print(total / len(items))


x = summary['x']
summary['total'] = 'total'


s: Summary = {'total': 10}


class Summary2(TypedDict, total=False):
    total: int
    title: str
    items: list[str]


s2: Summary2 = {'total': 10}
s3: Summary2 = {}


class Summary3(TypedDict):
    total: int
    title: str


class Summary4(Summary3, total=False):
    items: list[str]


s4: Summary4 = {}
s5: Summary4 = {'total': 10, 'title': 'Title'}



from typing import Required, NotRequired


class Summary5(TypedDict):
    total: Required[int]
    title: str
    items: NotRequired[list[str]]


s6: Summary5 = {}
s7: Summary4 = {'total': 10, 'title': 'Title'}
