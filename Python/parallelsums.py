"""
Parallel Sums
HIDE QUESTION
Have the function ParallelSums(arr) take the array of integers stored in arr which will 
always contain an even amount of integers, and determine how they can be split into two 
even sets of integers each so that both sets add up to the same number. If this is impossible 
return -1. If it's possible to split the array into two sets, then return a string 
representation of the first set followed by the second set with each integer separated 
by a comma and both sets sorted in ascending order. The set that goes first is the set
 with the smallest first integer.

For example: if arr is [16, 22, 35, 8, 20, 1, 21, 11], 
then your program should output 1,11,20,35,8,16,21,22
"""


from itertools import combinations
def ParallelSums(arr):
  if sum(arr)%2: return -1
  arr.sort()
  comb = combinations(arr,len(arr)//2)
  result = [list(i) for i in comb if sum(i)==sum(arr)//2]
  return ",".join(map(str,sum(result,[])))

  


print(ParallelSums(input()))