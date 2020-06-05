"""
Sometimes, you want a change of pace.
Sometimes, you want something different, yet familiar.
Sometimes, you want to call functions using square brackets instead.
"""

from functools import update_wrapper
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
    _func: Callable  # Under-the-hood callback function.
    def __init__(self, func: Callable) -> None:
        self._func = func
        update_wrapper(self, self._func)
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
        """Returns the argument incremented by 1."""
        return z+1
    assert increment.__name__ == "increment"
    assert increment.__doc__ == """Returns the argument incremented by 1."""
    assert increment.__annotations__ == {
        "z": int,
        "return": int
    }
    assert increment[1] == 2

    @Sbunction
    def add(a: int, b: int) -> int:
        """Returns the sum of the two arguments."""
        return a+b
    assert add[1, 2] == 3

    @Sbunction
    def scale(vector: Tuple[int, ...], scalar: int = 2) -> Tuple[int, ...]:
        """Returns the vector scaled by the scalar."""
        return tuple(i*scalar for i in vector)
    # Use a comma to avoid unpacking a single Tuple argument!
    assert scale[(1, 2, 3),  ] == (2, 4, 6)
    assert scale[(142857,), 0] == (0,)

    @Sbunction
    def sayhi() -> str:
        """Returns a greeting to the world."""
        return "Hello World!"
    # Use an empty Tuple to call a Sbunction with no arguments!
    assert sayhi[()] == "Hello World!"

    # Call Sbunction with square brackets to decorate a predefined function!
    print = Sbunction[print]

    print["Passed all checks.", "Have sbun!"]
