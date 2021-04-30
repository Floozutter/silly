"""
exploiting a Python quirk with UnboundLocalError to make significant code after a return!
inspired by:
- Eli Bendersky's "Understanding UnboundLocalError in Python":
  https://eli.thegreenplace.net/2011/05/15/understanding-unboundlocalerror-in-python/
- mCoding's "Variable Lookup Weirdness in Python":
  https://youtu.be/9v8eu4MOet8
"""

def a() -> bool:
    try:
        badname
    except UnboundLocalError:
        return True
    except NameError:
        pass
    return False

def b() -> bool:
    try:
        badname
    except UnboundLocalError:
        return True
    except NameError:
        pass
    return False
    badname = ...

if __name__ == "__main__":
    for f in (a, b):
        print(f"{f.__name__}: {f()}")
