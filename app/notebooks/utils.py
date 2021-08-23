def remove_csrf(d):
    if isinstance(d, dict):
        return {k: remove_csrf(v) for k, v in d.items() if k != 'csrf_token'}
    if isinstance(d, list):
        return [remove_csrf(v) for v in d]
    return d
