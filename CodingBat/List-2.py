List-2 > count_evens


# Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.
#
# count_evens([2, 1, 2, 3, 4]) → 3
# count_evens([2, 2, 0]) → 3
# count_evens([1, 3, 5]) → 0



# def count_evens(nums):
#   count = 0
#
#   for i in range(0, len(nums), 1):
#
#     if nums [i] % 2 == 0:
#       count = count +1
#
#   return count

  
  
# Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.

# big_diff([10, 3, 5, 6]) → 7
# big_diff([7, 2, 10, 9]) → 8
# big_diff([2, 10, 7, 2]) → 8
#
#
# def big_diff(nums):
#   return max(nums) - min(nums)

  
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
  
  
  # def big_diff(nums):
  # maxv = nums[0]
  # minv = nums[0]
  #
  # for i in range(0, len(nums),1):
  #
  #  maxv = max(maxv,nums[i])
  #  minv = min(minv,nums[i])
  #
  # return maxv - minv
  
# Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may assume that the array is length 3 or more.

centered_average([1, 2, 3, 4, 100]) → 3
centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
centered_average([-10, -4, -2, -4, -2, 0]) → -3


def centered_average(nums):
  return (sum(nums) - min(nums) - max(nums)) / (len(nums)- 2)
  
  def centered_average(nums):
  nums.sort()
  return (sum(nums) - nums[0] - nums[len(nums)- 1]) / (len(nums)- 2)
  
  def centered_average(nums):
  sum = 0
  largest = nums[0]
  smallest = nums[0]
  
  for i in range(0, len(nums), 1):
    sum = sum + nums[i]
    largest = max(largest, nums[i])
    smallest = min(smallest, nums[i])
  
  return (sum - largest - smallest) / (len(nums)- 2)

  # Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.
  sum13([1, 2, 2, 1]) → 6
  sum13([1, 1]) → 2
  sum13([1, 2, 2, 1, 13]) → 6
  
  def sum13(nums):
  sum = 0
  i = 0
  while (i < len(nums)):
    if (nums[i] != 13):
      sum = sum + nums[i]
    else:
      i = i + 1
    i = i + 1
  return sum 

  


  