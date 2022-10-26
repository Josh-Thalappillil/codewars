# Very simple, given an integer or a floating-point number, find its opposite.

def opposite(number):
    if number > 0:
        return -abs(number)
    elif number < 0:
        return abs(number)
    else:
        return number


#SUGGESTED METHOD

def opposite2(number):
    return -number

opposite2(10)