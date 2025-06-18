import math as m

def func(a, b, c, d):
    try:
        y = (m.sqrt(a-b))/(c-d)
    except ZeroDivisionError:
        result = 'there is zero divizion'
        raise ZeroDivisionError
    except ValueError:
        result = "can't divide zero without complex"
    except TypeError:
        result = 'this is not a number'
    else:
        result = round(y,4)
    return result