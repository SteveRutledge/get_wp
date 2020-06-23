# (generated with --quick)

from typing import Any, Callable, Type, TypeVar

API_URL: str
click: module
desert: Any
marshmallow: Any
requests: module
schema: Any

_T = TypeVar('_T')

class Page:
    __doc__: str
    extract: str
    title: str
    def __init__(self, title: str, extract: str) -> None: ...

@overload
def dataclass(_cls: Type[_T]) -> Type[_T]: ...
@overload
def dataclass(*, init: bool = ..., repr: bool = ..., eq: bool = ..., order: bool = ..., unsafe_hash: bool = ..., frozen: bool = ...) -> Callable[[Type[_T]], Type[_T]]: ...
def random_page(language: str = ...) -> Page: ...
