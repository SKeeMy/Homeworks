

def cache(times: int):
    if times < 0:
        raise ValueError("Times argument must be a positive integer")
    cached = {'value': None, 'count': times}

    def decorator(func: callable):
        def wrapper(*args, **kwargs):
            nonlocal cached
            if cached['count'] > 0 and cached.get('value'):
                cached['count'] -= 1
                is_cached_call = True
                return (cached['value'], is_cached_call)
            else:
                (cached['value'], is_cached_call) = func(*args, **kwargs)
                return (cached['value'], is_cached_call)
        return wrapper
    return decorator
