from typing import List, Set, Dict, Tuple
x0: List[int] = [1]
x1: Set[int] = {6, 7}
x2: Dict[str, float] = {"field": 2.0}
x3: Tuple[int, str, float] = (3, "yes", 7.5)
x4: Tuple[int, ...] = (1, 2, 3)

from typing import Union, Optional

# On Python 3.10+, use the | operator when something could be one of a few types
x5: list[int | str] = [3, 5, "test", "fun"]  # Python 3.10+
# On earlier versions, use Union
x6: list[Union[int, str]] = [3, 5, "test", "fun"]

# Use X | None for a value that could be None on Python 3.10+
# Use Optional[X] on 3.9 and earlier; Optional[X] is the same as 'X | None'
x7: str | None = "something" if 1 == 1 else None
if x7 is not None:
    # Mypy understands x won't be None here because of the if-statement
    print(x7.upper())
# If you know a value can never be None due to some logic that mypy doesn't
# understand, use an assert
assert x7 is not None
print(x7.upper())