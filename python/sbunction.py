"""
Sometimes, you want a change of pace.
Sometimes, you want something different, yet familiar.
Sometimes, you want to call functions using square brackets instead.
"""

from typing import Any, Union, Callable, Tuple


class Sbunction:
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

class Sbfunction(Sbunction):
    """
    Sbfunctions are Sbunctions that can also be called with parentheses.
    """
    def __init__(self, func: Callable) -> None:
        super().__init__(func)
    def __call__(self, *args, **kwargs) -> Any:
        return self._func(*args, **kwargs)


def sbunction(func: Callable) -> Sbunction:
    """
    Decorator to make a Sbunction out of a normal ol' funcion.
    """
    return Sbunction(func)
sbunction = Sbfunction(sbunction)


if __name__ == "__main__":
    @sbunction
    def increment(z: int) -> int:
        return z+1
    assert increment[1] == 2

    @sbunction
    def add(a: int, b: int) -> int:
        return a+b
    assert add[1, 2] == 3

    @sbunction
    def scale(vector: Tuple[int, ...], scalar: int = 2) -> Tuple[int, ...]:
        return tuple(i*scalar for i in vector)
    # Use a comma to avoid unpacking a single Tuple argument!
    assert scale[(1, 2, 3),  ] == (2, 4, 6)
    assert scale[(142857,), 0] == (0,)

    @sbunction
    def sayhi() -> str:
        return "Hello World!"
    # Use an empty Tuple to call a Sbunction with no arguments!
    assert sayhi[()] == "Hello World!"

    # Use sbunction as a Sbunction to decorate an already existing function!
    print = sbunction[print]

    print["Passed all checks.", "Have sbun!"]
