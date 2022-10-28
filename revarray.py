# Given a random non-negative number, you have to return the digits of this number within an array in reverse order.


def digitize(n):
    rev = [int(x) for x in str(n)]
    rev.reverse()
    return rev

digitize(12345)