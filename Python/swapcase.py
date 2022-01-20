"""
Swap Case
Have the function SwapCase(str) take the str parameter and swap the case of each character. 
For example: if str is "Hello World" the output should be hELLO wORLD. Let numbers and symbols stay the way they are.
"""

def SwapCase(strParam):
  strParam = list(strParam)
  
  for index in range(0,len(strParam)):
    if strParam[index] == strParam[index].lower():
      strParam[index] = strParam[index].upper()
    else:
      strParam[index] = strParam[index].lower()
  return "".join(strParam) 
  


print (SwapCase(input()))