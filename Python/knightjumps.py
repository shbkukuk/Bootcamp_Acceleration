import re
from itertools import product
def KnightJumps(strParam):
  strnum = re.findall(r'\d',strParam)
  x = int(strnum[0])
  y = int(strnum[1])
  moves = list(product([x-1,x+1],[y-2,y+2])) + list(product([x-2,x+2],[y-1,y+1]))
  moves = [(x,y) for x,y in moves if x>0 and y>0 and x<8 and y<8 ]
  
  
  return len(moves)

# keep this function call here 
print(KnightJumps(input()))