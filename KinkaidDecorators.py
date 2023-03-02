import logging
from typing import Callable, Any
import functools
import traceback
"""
Based on an example by Arjan of arjancodes.com: https://www.youtube.com/watch?v=QH5fw9kxDQA 
"""
def log_start_stop_method(func: Callable[..., Any]) -> Callable[..., Any]:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        indent = "\t"*len(traceback.extract_stack())
        logging.info(f"{indent}Starting method {func.__name__}\n({args})")
        value = func(*args, **kwargs)
        logging.info(f"{indent}Finishing method: {func.__name__}")
        return value
    return wrapper

