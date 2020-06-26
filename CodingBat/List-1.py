# Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more.

# first_last6([1, 2, 6]) → True
# first_last6([6, 1, 2, 3]) → True
# first_last6([13, 6, 1, 2, 3]) → False


# def first_last6(nums):
#   if 6 == nums[0] or 6 == nums[-1]:
#     return True
#   return False
#
  
# def first_last6(nums):
#   x = len(nums)
#   if (nums[0] == 6 or nums[x -1] == 6):
#     return True
#   return False
  
  
  
# Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.

# same_first_last([1, 2, 3]) → False
# same_first_last([1, 2, 3, 1]) → True
# same_first_last([1, 2, 1]) → True
#

  
# def same_first_last(nums):
#   l = len(nums)
#
#   if (l == 0):
#     return False
#
#   if (nums[0] == nums[l -1]):
#     return True
#   return False
  
  
# def same_first_last(nums):
#   l = len(nums)
#   if (l > 0 and nums[0] == nums[l -1]):
#     return True
#   return False
#
  
# def same_first_last(nums):
#   return len(nums) > 0 and nums[0] == nums[len(nums) -1]
#
  
  
# Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.

# make_pi() → [3, 1, 4]


# def make_pi():
#   list = [3, 1, 4]
#   return list


#  Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element. Both arrays will be length 1 or more.

# common_end([1, 2, 3], [7, 3]) → True
# common_end([1, 2, 3], [7, 3, 2]) → False
# common_end([1, 2, 3], [1, 3]) → True


# def common_end(a, b):
#   if a[0] == b[0] or a[len(a) -1] == b[len(b)-1]:
#     return True
#   return False

  
 # Given an array of ints length 3, return the sum of all the elements.

# sum3([1, 2, 3]) → 6
# sum3([5, 11, 2]) → 18
# sum3([7, 0, 0]) → 7

# def sum3(nums):
#   sum = 0
#
#   for i in range(0, len(nums), 1):
#     sum = sum + nums[i]
#
#   return sum

  
  
  
 # Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.

rotate_left3([1, 2, 3]) → [2, 3, 1]
rotate_left3([5, 11, 9]) → [11, 9, 5]
rotate_left3([7, 0, 0]) → [0, 0, 7]


def rotate_left3(nums):
  new_nums = [nums[1], nums[2], nums[0]]
  return new_nums
