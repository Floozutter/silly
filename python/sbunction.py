"""
Sometimes, you want a change of pace.
Sometimes, you want something different, yet familiar.
Sometimes, you want to call functions using square brackets instead.
"""

from typing import Any, Union, Callable, Tuple


class Sblass(type):
    """
    Classes of Sblass can be called with square brackets.
    """
    def __getitem__(self, key: Union[Tuple, Any]):
        """
        Passes the key argument to __call__.
        Tuple arguments are always unpacked when passed.
        """
        if isinstance(key, tuple): return self.__call__(*key)
        else: return self.__call__(key)

class Sbunction(metaclass=Sblass):
    """
    Sbunctions are functions called with square brackets.
    """
    _func: Callable  # under-the-hood function to call
    def __init__(self, func: Callable) -> None:
        self._func = func
    def __getitem__(self, key: Union[Tuple, Any]) -> Any:
        """
        Handles passing the key argument to the under-the-hood function.
        Tuple arguments are always unpacked when passed.
        """
        if isinstance(key, tuple): return self._func(*key)
        else: return self._func(key)


if __name__ == "__main__":
    @Sbunction
    def increment(z: int) -> int:
        return z+1
    assert increment[1] == 2

    @Sbunction
    def add(a: int, b: int) -> int:
        return a+b
    assert add[1, 2] == 3

    @Sbunction
    def scale(vector: Tuple[int, ...], scalar: int = 2) -> Tuple[int, ...]:
        return tuple(i*scalar for i in vector)
    # Use a comma to avoid unpacking a single Tuple argument!
    assert scale[(1, 2, 3),  ] == (2, 4, 6)
    assert scale[(142857,), 0] == (0,)

    @Sbunction
    def sayhi() -> str:
        return "Hello World!"
    # Use an empty Tuple to call a Sbunction with no arguments!
    assert sayhi[()] == "Hello World!"

    # Call Sbunction with square brackets to decorate a predefined function!
    print = Sbunction[print]

    print["Passed all checks.", "Have sbun!"]
