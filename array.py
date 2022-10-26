# Given an array of integers.
# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 
# 0 is neither positive nor negative.
# If the input is an empty array or is null, return an empty array.

from ipaddress import summarize_address_range


def count_positives_sum_negatives(arr):
    
    poscount = 0
   
    for posnum in arr:
        if posnum > 0:
            poscount +=1
    
count_positives_sum_negatives([-5, -1, 0, 1, 3, 4, 5])
# Could only get up to here

 #SUGGESTED ANSWER:           
def count_positives_sum_negatives(arr):
    if not arr: return []
    pos = 0
    neg = 0
    for x in arr:
      if x > 0:
          pos += 1
      if x < 0:
          neg += x
    return [pos, neg]



    


