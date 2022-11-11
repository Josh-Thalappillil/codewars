#In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?

def make_negative( number ):
    if number > 0:
        return number * (-1)
    elif number < 0:
        return number
    else: 
        return 0



#better solution from codewars
def make_negative2( number ):
    print(-abs(number))


make_negative(13)
make_negative2(23)