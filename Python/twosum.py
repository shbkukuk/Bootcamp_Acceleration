"""
Two Sum
Have the function TwoSum(arr) take the array of integers stored in arr, 
and determine if any two numbers (excluding the first element) in 
the array can sum up to the first element in the array. For example: 
if arr is [7, 3, 5, 2, -4, 8, 11], then there are actually two pairs 
that sum to the number 7: [5, 2] and [-4, 11]. Your program should return all pairs, 
with the numbers separated by a comma, in the order the first number appears in the array. 
Pairs should be separated by a space. So for the example above, your program would 
return: 5,2 -4,11
"""
def TwoSum(arr):
  first_element = arr.pop(0)
  lst_arr = []
  for i in range(0,len(arr)):
    k = i+1 
    for j in range(k,len(arr)):
      if first_element == (arr[i]+arr[j]):
        lst_arr.append(str(arr[i])+','+str(arr[j]))
        
  
  if lst_arr != []:
    return " ".join(lst_arr)
  else:
    return -1

print(TwoSum([0,2,5,46]))