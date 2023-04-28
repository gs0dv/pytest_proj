def get_val(collection, key=None, default='git'):
    if not key:
        return None

    return collection[key] if collection else default
