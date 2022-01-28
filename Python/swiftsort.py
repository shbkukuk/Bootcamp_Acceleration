def SwitchSort(arr):
  swap = 0
  visited = [False for i in range(len(arr))]
  
  for i in range(len(arr)):
    j = i
    counter = 0
    while not visited[j]:
      visited[j] = True
      j = arr[j]-1
      print(visited)
      counter = counter+1
    if counter != 0:
      swap = swap+(counter-1)


  # code goes here
  return swap

# keep this function call here 
print (SwitchSort([5,3,1,2,4]))
a= [0,1,2,3,4,5,6,7,8,9]
print(a[::3])
