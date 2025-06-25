from parts.constant import *
def protection(method):
    def wrapper(self, *args, **kwargs):
        if kwargs.get('user_name') == ADMIN_USERNAME:
            result = method(self, *args, **kwargs)
            return result
        else:   
            print(UNKNOWN_COMMAND)
    return wrapper
