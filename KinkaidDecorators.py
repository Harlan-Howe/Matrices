import logging
from typing import Callable, Any

import functools


def log_start_stop_method(func: Callable[..., Any]) -> Callable[..., Any]:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        logging.info(f"Starting method {func.__name__}({args})")
        value = func(*args, **kwargs)
        logging.info(f"Finishing method: {func.__name__}")
        return value
    return wrapper

