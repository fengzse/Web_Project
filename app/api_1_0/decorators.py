from flask import g
from functools import wraps
from .errors import forbidden


def permission_required(permission):
    def decorators(func):
        @wraps(func)
        def decor_function(*args, **kwargs):
            if not g.current_user.can(permission):
                return forbidden('Insufficient permissions')
            return func(*args, **kwargs)

        return decor_function

    return decorators
