# Given two integers a and b, which can be positive or negative, 
# find the sum of all the integers between and including them and return it. 
# If the two numbers are equal return a or b.
# Note: a and b are not ordered!

# find the numbers between a and b
# use the range function?
# sum those values
# if value is equal return a or b (so ill need a if statement)


# MY CODE:
def get_sum(a, b):
    if a != b:
        total = sum(range(a, b))
        print(total)
    else:
        print(a)

get_sum(0, 1)

#SUGGESTED ANSWER


