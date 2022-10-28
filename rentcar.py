# After a hard quarter in the office you decide to get some rest on a vacation. 
# So you will book a flight for you and your girlfriend and try to leave all the mess behind you.
# You will need a rental car in order for you to get around in your vacation. 
# The manager of the car rental makes you some good offers.

# Every day you rent the car costs $40. 
# If you rent the car for 7 or more days, you get $50 off your total. 
# Alternatively, if you rent the car for 3 or more days, you get $20 off your total.

# Write a code that gives out the total amount for different days(d).

# MY SOLUTION
def rental_car_cost(d):
    cost = d * 40

    if d <= 2:
        cost = d * 40
        return cost
    
    elif d <= 6:
        cost = (d * 40) - 20
        return cost
    
    else:
        cost = (d * 40) - 50
        return cost


rental_car_cost(4)


# Suggested way:

def rental_car_cost(d):
    result = d * 40
    if d >= 7:
        result -= 50
    elif d >= 3:
        result -= 20
    return result