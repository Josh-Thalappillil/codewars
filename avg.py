# Write a function which calculates the average of the numbers in a given list.
# Note: Empty arrays should return 0.

def find_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

find_average([2, 2, 4, 2, 4])

