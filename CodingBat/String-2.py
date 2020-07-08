String-2 > double_char

# Given a string, return a string where for every char in the original, there are two chars.

# double_char('The') → 'TThhee'
# double_char('AAbb') → 'AAAAbbbb'
# double_char('Hi-There') → 'HHii--TThheerree'

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


def double_char(str):
  return str[0:1]*2 + str[1:2]*2 + str[2:3]*2 + str[3:4]*2 + str[4:5]*2 + str[5:6]*2 + str[6:7]*2 + str[7:8]*2 #bad long way
   

# Return the number of times that the string "hi" appears anywhere in the given string.

# count_hi('abc hi ho') → 1
# count_hi('ABChi hi') → 2
# count_hi('hihi') → 2

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
  
  
# Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.

# count_code('aaacodebbb') → 1
# count_code('codexxcode') → 2
# count_code('cozexxcope') → 2
#

def count_code(str):
  count = 0
  
  for i in range(0, len(str) - 3, 1):
    
    if (str[i] == 'c' and str [i+1] == 'o' and str [i+3] == 'e'):
      count = count + 1
      
  return count

# Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string.

# end_other('Hiabc', 'abc') → True
# end_other('AbC', 'HiaBc') → True
# end_other('abc', 'abXabc') → True


def end_other(a, b):
  a = a.lower()
  b = b.lower()
  
  lstr = a
  sstr = b
  
  if len(b) > len(a):
    lstr = b
    sstr = a
    
  if sstr == lstr[len(lstr) - len(sstr): len(lstr)]:
    return True
  return False

# Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.

# xyz_there('abcxyz') → True
# xyz_there('abc.xyz') → False
# xyz_there('xyz.abc') → True


def xyz_there(str):
  return str.count("xyz") - str.count(".xyz") > 0

def xyz_there(str):
  return str.replace(".xyz", "").find("xyz") >= 0


def xyz_there(str):
  if len(str) >= 3 and str[0:3] == "xyz":
    return True

  for i in range(1, len(str) - 2, 1):
    if str[i: i + 3] == "xyz" and str[i - 1] != ".":
      return True
  return False
