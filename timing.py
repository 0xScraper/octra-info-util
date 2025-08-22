from collections.abc import Callable
from functools import wraps
from time import perf_counter
from typing import Any


def get_time(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:

        start_time: float = perf_counter()
        result: Any = func(*args, **kwargs)
        end_time: float = perf_counter()

        print(f'Data fetching completed in {end_time - start_time:.3f} seconds.\n')
        return result

    return wrapper

