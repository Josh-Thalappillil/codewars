# Complete the function so that it finds the average of the three scores 
# passed to it and returns the letter value associated with that grade.

def get_grade(s1, s2, s3):
    
    avg = (s1 + s2 + s3) / 3
    
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    elif avg < 60:
        return "F"


