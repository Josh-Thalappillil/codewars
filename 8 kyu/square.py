# Complete the square sum function so that it squares each number passed into it and then sums the results together.

# For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9.

# MY SOLUTION:
def square_sum(numbers):
    num = [x ** 2 for x in numbers]
    print(sum(num))
    return sum(num)

# Should equal 9
square_sum([1, 2, 2])


# Suggested method:
def suggested_method(numbers):
    return sum(x ** 2 for x in numbers)


