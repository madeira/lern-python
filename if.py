__author__ = 'madeira'
def average ( x, y, z):
    if x > y:
        if x > z:
            if z > y:
                return z
            else:
                return y
        else:
            return x
    elif x > z:
        return x
    elif z > y:
        return y
    else:
        return z

assert average (1,3,6) == 3
assert average (1,6,3) == 3
assert average (3,1,6) == 3
assert average (3,6,1) == 3
assert average (6,3,1) == 3
assert average (6,1,3) == 3


