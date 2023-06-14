from collections import Callable

def cache(func: Callable) -> Callable:
    cached_results = {}
    
    def cached_func(*args):
        if args in cached_results:
            return cached_results[args]
        else:
            result = func(*args)
            cached_results[args] = result
            return result
    
    return cached_func