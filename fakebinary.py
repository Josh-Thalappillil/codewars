# Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. 
# Return the resulting string.

def fake_bin(x):
    result = ""
    numstring = x
    
    for digit in numstring:
        
        if int(digit) >= 5:
            result += "1"
        elif int(digit) < 5:
            result += "0"
    return result


# Best practice method
def fake_bin2(x):
    return ''.join('0' if c < '5' else '1' for c in x)




