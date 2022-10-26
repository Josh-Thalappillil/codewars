#Given a non-empty array of integers, return the result of multiplying the values together in order.
# [1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24

def grow(arr):
    result = 1
    for number in arr:
        result *= number
    return result

grow([1, 3, 1])


