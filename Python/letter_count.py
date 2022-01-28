"""
Letter Count
Have the function LetterCount(str) take the str parameter being passed and 
return the first word with the greatest number of repeated letters. For example: 
"Today, is the greatest day ever!" should return greatest because it has 2 e's (and 2 t's) 
and it comes before ever which also has 2 e's. If there are no words with repeating letters return -1. 
Words will be separated by spaces.
"""
def LetterCount(strParam):
  list_str = strParam.split(" ")
  letter_words = {}
  for index in range(0,len(list_str)):
    word = list(list_str[index])
    count = 0
    for i in range(0,len(word)):
      k = i+1
      for j in range(k,len(word)):
        if word[i].lower()==word[j].lower():
          count += 1 
          letter_words["".join(word)] = count     
  letter = []
  for k,v in letter_words.items():
    letter.append([k,v])
  
  greatest = 0
  for i in range(0,len(letter)):
    if greatest < letter[i][1]: 
      greatest = letter[i][1]

  for j in range(0,len(letter)):
    if greatest == letter[j][1]:
      return "".join(letter[j][0])
  


  return -1 

print (LetterCount(input()))