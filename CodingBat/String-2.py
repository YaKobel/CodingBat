String-2 > double_char

# Given a string, return a string where for every char in the original, there are two chars.

double_char('The') → 'TThhee'
double_char('AAbb') → 'AAAAbbbb'
double_char('Hi-There') → 'HHii--TThheerree'


def double_char(str):
  result = ""
  
  for i in range(0,len(str),1):
    result = result + str[i] + str[i]
  return result


# Return the number of times that the string "hi" appears anywhere in the given string.

count_hi('abc hi ho') → 1
count_hi('ABChi hi') → 2
count_hi('hihi') → 2


def count_hi(str):
  count = 0
  
  for i in range(0, 1000, 1):
    if str[i:i+2] == "hi":
      count = count + 1
      
  return count

