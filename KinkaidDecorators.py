import logging
from typing import Callable, Any




def log_start_stop_method(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        logging.info(f"Starting method {func.__name__}")
        value = func(*args,**kwargs)
        logging.info(f"Finishing method: {func.__name__}")
        return value
    return wrapper

