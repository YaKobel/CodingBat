String-2 > double_char

# Given a string, return a string where for every char in the original, there are two chars.

double_char('The') → 'TThhee'
double_char('AAbb') → 'AAAAbbbb'
double_char('Hi-There') → 'HHii--TThheerree'

'''
def double_char(str):
  result = ""
  
  for i in range(0,len(str),1):
    result = result + str[i] + str[i]
  return result
'''
  
def double_char(str):
  result = ""
  
  for i in range(len(str)):
    result = result + str[i] + str[i]
  return result

  

# Return the number of times that the string "hi" appears anywhere in the given string.

count_hi('abc hi ho') → 1
count_hi('ABChi hi') → 2
count_hi('hihi') → 2

'''
def count_hi(str):
  count = 0
  
  for i in range(0, 1000, 1):    #   for i in range(0, len(str) - 1, 1):
    if str[i:i+2] == "hi":
      count = count + 1
      
  return count
'''
  
'''
def count_hi(str):
  ctr = 0
  
  for i in range(0, len(str), 1):
    temp = str[i:i+2]  # i + 2 - i = 2 
    if temp == "hi":
      ctr = ctr + 1
      
  return ctr

  
def count_hi(str):
  ctr = 0
  
  for i in range(0, len(str)-1, 1):
    temp = str[i] + str[i+1] 
    if temp == "hi":
      ctr = ctr + 1
      
  return ctr

'''  
  
def count_hi(str):
  str1 = str.replace("hi","")
  return (len(str) - len(str1))/2  
  
  
  
'''  
def count_hi(str):
  return str.count('hi')
'''  
  
# Return True if the string "cat" and "dog" appear the same number of times in the given string.

cat_dog('catdog') → True
cat_dog('catcat') → False
cat_dog('1cat1cadodog') → True

'''
def cat_dog(str):
  return str.count("cat") == str.count("dog")
'''

def cat_dog(str):
  cstr = str.replace("cat","")
  dstr = str.replace("dog","")
  
  if (len(cstr) == len(dstr)):
    return True
  return False
  
  
def cat_dog(str):
  no_cat = str.replace("cat","")
  no_dog = str.replace("dog","")
  
  return len(no_cat) == len(no_dog)

  
  
'''  
def cat_dog(str):
  dog_count = 0
  cat_count = 0
  
  for i in range(0,len(str), 1):  #len(str) - ((reading frame lenght) -1)
    if str[i: i + 3] == "cat":
      cat_count = cat_count + 1
    if str[i: i + 3] == "dog":
      dog_count = dog_count + 1
      
  return dog_count == cat_count
  '''
  
  