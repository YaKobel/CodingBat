# Given a string and a non-negative int n, return a larger string that is n copies of the original string.
#
# string_times('Hi', 2) → 'HiHi'
# string_times('Hi', 3) → 'HiHiHi'
# string_times('Hi', 1) → 'Hi'


# def string_times(str, n):
#   return str * n


# def string_times(str, n):
#   result = ""
#   for i in range(n):  # range(n) is [0, 1, 2, .... n-1]
#     result = result + str  # could use += here
#   return result


# Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;
#
# front_times('Chocolate', 2) → 'ChoCho'
# front_times('Chocolate', 3) → 'ChoChoCho'
# front_times('Abc', 3) → 'AbcAbcAbc'


# def front_times(str, n):
#   return n*(str[:3])


# def front_times(str, n):
#   return str[0:3] * n


# def front_times(str, n):
#   front_len = 3
#   if front_len > len(str):
#     front_len = len(str)
#   front = str[:front_len]
#
#   result = ""
#   for i in range(n):
#     result = result + front
#   return result
  
  

# Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".
#
# string_bits('Hello') → 'Hlo'
# string_bits('Hi') → 'H'
# string_bits('Heeololeo') → 'Hello'


# def string_bits(str):
#   return str[::2]


# def string_bits(str):
#   result = ""
#   # Many ways to do this. This uses the standard loop of i on every char,
#   # and inside the loop skips the odd index values.
#   for i in range(len(str)):
#     if i % 2 == 0:
#       result = result + str[i]
#   return result

# def string_bits(str):
#   result = ""
#   for x in xrange(0,len(str),2):
#     result += str[x]
#   return result

  

# Given a non-empty string like "Code" return a string like "CCoCodCode".
#
# string_splosion('Code') → 'CCoCodCode'
# string_splosion('abc') → 'aababc'
# string_splosion('ab') → 'aab'
#
# def string_splosion(str):
#   if len(str) == 1:
# 	  return str
#
#   string_1 = ""
#   for iteration in range(len(str)):
#   	string_1 += str[:1+iteration]
#   return string_1

  
  
# def string_splosion(str):
#   result = ""
#   for i in range(len(str)):
#     result = result + str[:i+1]
#   return result

  
# def string_splosion(str):
#   s='';
#   for x in range (len(str)):
#     for y in range (x):
#       s = s +str[y];
#     s =s + str[x];
#   return s;

  
  
  
# def string_splosion(str):
#   res='';
#   for i in range(len(str)+1):
#     res = res + str[0:i];
#   return res
  
  
 # Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).

# last2('hixxhi') → 1
# last2('xaxxaxaxx') → 1
# last2('axxxaaxx') → 2

# # 1 VARIANT
# def last2(str):
#   if len(str) < 2:
#     return 0
#
#   ctr = 0
#   compStr = str[len(str) -2: len(str)]
#
#   for i in range(0,len(str)-1, 1):
#     if str[i:i+2] == compStr:
#       ctr = ctr + 1
#   return ctr -1

# # 2 VARIANT
# def last2(str):
#   if len(str) < 2: # This is necessary if proramming in Java, many other languages
#     return 0
#
#   ctr = 0
#   compStr = str[len(str) -2: len(str)]
#
#   for i in range(len(str)-2):
#     if str[i:i+2] == compStr:
#       ctr = ctr + 1
#   return ctr
  
#  # 3 VARIANT
# def last2(str):
#   ctr = 0
#   compStr = str[len(str) -2: len(str)] # taking advantage of Python
#
#   for i in range(0,len(str)-2, 1): # i < len(str) -2, i < 6 -2 = 4
#     if str[i:i+2] == compStr:
#       ctr = ctr + 1
#   return ctr
  

#  def last2(str):
# # Screen out too-short string case.
#   if len(str) < 2:
#     return 0
#
  # last 2 chars, can be written as str[-2:]
  # last2 = str[len(str)-2:]
  # count = 0
  
  # Check each substring length 2 starting at i
#   for i in range(len(str)-2):
#     sub = str[i:i+2]
#     if sub == last2:
#       count = count + 1
#
#   return count
#
# # not work all (idea for task)
# def last2(str):
#   compStr = str[len(str) -2: len(str)]
#   newStr = str.replace(compStr, "")
#   return (len(str)- len(newStr))/2 -1
  
  
#  Given an array of ints, return the number of 9's in the array.

# array_count9([1, 2, 9]) → 1
# array_count9([1, 9, 9]) → 2
# array_count9([1, 9, 9, 3, 9]) → 3
#
#
# def array_count9(nums):
#   crt = 0
#   for i in range(0, len(nums),1):
#     if nums[i] == 9:
#       crt = crt + 1;
#   return crt
#
#
# def array_count9(nums):
#   crt = nums.count(9)
#   return crt
#
#
#
# def array_count9(nums):
#   count = 0
#   for num in nums:
#     if num == 9:
#       count = count + 1
#   return count
 
  
  
  
#  Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.

# array_front9([1, 2, 9, 3, 4]) → True
# array_front9([1, 2, 3, 4, 9]) → False
# array_front9([1, 2, 3, 4, 5]) → False
#
# def array_front9(nums):
#   l = 4
#   if len(nums) < 4:
#     l = len(nums)
#
#   for i in range(0,l,1):
#     if nums[i] == 9:
#       return True
#   return False
#
#
#
# def array_front9(nums):
#   return 9 in nums[0:4]
#
#
# def array_front9(nums):
#   # First figure the end for the loop
#   end = len(nums)
#   if end > 4:
#     end = 4
#
#   for i in range(end):  # loop over index [0, 1, 2, 3]
#     if nums[i] == 9:
#       return True
#   return False