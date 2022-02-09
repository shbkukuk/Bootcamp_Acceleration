def ArrayCouples(arr):
  pairs = []
  for i in range(0,len(arr),2):
    pairs.append([arr[i], arr[i+1]])
  for i in pairs:
      if i[::-1] in pairs:
          pairs.remove(i)
          pairs.remove(i[::-1])
  return pairs  

def ArrayCouples2(arr):
  
  pairs = []
  allPairs = []
  for i in range(0,len(arr),2):
    j = i + 1



print(ArrayCouples([3,3,1,2,2,1]))
print(ArrayCouples2([3,3,1,2,2,1]))