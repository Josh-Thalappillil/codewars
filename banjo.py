# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!

# The function takes a name as its only argument, and returns one of the following strings:
# name + " plays banjo" 
# name + " does not play banjo"


# create a function with parameter of name
# create an if statement argument which identifies if name contains a capital or lowercase r
# return the name + string depending on if statment
# define name parameter 

def are_you_playing_banjo(name):
    if name.startswith("R"):
        print(name + " plays banjo")
    if name.startswith("r"):
        print(name + " plays banjo")
    else:
        print(name + " does not play banjo")

are_you_playing_banjo("Joshua")