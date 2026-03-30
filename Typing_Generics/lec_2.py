x1: int = 1
x2: float = 1.0
x3: bool = True
x4: str = "test"
x5: bytes = b"test"

# For collections on Python 3.9+, the type of the collection item is in brackets
x6: list[int] = [1]
x7: set[int] = {6, 7}

# For mappings, we need the types of both keys and values
x8: dict[str, float] = {"field": 2.0}  # Python 3.9+

# For tuples of fixed size, we specify the types of all the elements
x9: tuple[int, str, float] = (3, "yes", 7.5)  # Python 3.9+

# For tuples of variable size, we use one type and ellipsis
x0: tuple[int, ...] = (1, 2, 3) 