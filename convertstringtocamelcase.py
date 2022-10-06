import re

def to_camel_case(text):
    if text == "":
        return ""

    listofw = re.split("-|_",text)
    result = ""
    for i in listofw:
        result += str(i).capitalize()

    if text[0].islower():
        result = result[0].lower() + result[1:]

    print(result)    
    return result

    

    




to_camel_case("the-steal-warrior")
to_camel_case("The_steal_warrior")
