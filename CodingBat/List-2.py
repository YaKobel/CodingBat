List-2 > count_evens


Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.

count_evens([2, 1, 2, 3, 4]) → 3
count_evens([2, 2, 0]) → 3
count_evens([1, 3, 5]) → 0



def count_evens(nums):
  count = 0
  
  for i in range(0, len(nums), 1):
    
    if nums [i] % 2 == 0:
      count = count +1
      
  return count

  
  
# Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.

big_diff([10, 3, 5, 6]) → 7
big_diff([7, 2, 10, 9]) → 8
big_diff([2, 10, 7, 2]) → 8


def big_diff(nums):
  return max(nums) - min(nums) 

  
  '''
  def big_diff(nums):
  maxv = nums[0]
  minv = nums[0]
  
  for i in range(0, len(nums),1):
    
    if maxv < nums[i]:
      maxv = nums [i]
    if minv > nums [i]:
      minv = nums[i]
  
  return maxv - minv 
  '''
  
  
  def big_diff(nums):
  maxv = nums[0]
  minv = nums[0]
  
  for i in range(0, len(nums),1):
    
   maxv = max(maxv,nums[i])
   minv = min(minv,nums[i])
   
  return maxv - minv 
  
  
