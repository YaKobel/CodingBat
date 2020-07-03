Logic-2 > make_bricks

We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each). Return True if it is possible to make the goal by choosing from the given bricks. This is a little harder than it looks and can be done without any loops. See also: Introduction to MakeBricks

make_bricks(3, 1, 8) → True
make_bricks(3, 1, 9) → False
make_bricks(3, 2, 10) → True

# Correct for more than half the tests
def make_bricks(small, big, goal):
  return small + (big*5) >= goal
  
  
def make_bricks(small, big, goal):
  return small + big*5 >= goal and goal%5 - small <= 0 
  
  
# Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, it does not count towards the sum.

lone_sum(1, 2, 3) → 6
lone_sum(3, 2, 3) → 2
lone_sum(3, 3, 3) → 0

'''
def lone_sum(a, b, c):
  
  if a == b == c:
    return 0
  if a == b:
    return c
  if a == c:
    return b
  if b == c:
    return a
  return a+b+c
  '''
  
  '''
  def lone_sum(a, b, c):
  
  sum = a+b+c
  if a == b:
    if a == c:
        sum -= 3 * a
    else:
        sum -= 2 * a
  elif b == c:
    sum -= 2 * b
  elif a == c:
    sum -= 2 * a
  return sum
'''
  '''
def lone_sum(a, b, c):
  
  if a != b and b != c and c != a:
    return a + b + c

  elif a == b == c:
    return 0 

  elif a == b:
    return c
  elif b == c:
    return a
  elif c == a:
    return b 
  '''
  '''
def lone_sum(a, b, c):

  z = (a,b,c)
  x = []
  for item in z:
      if z.count(item)==1:
          x.append(item)
  return sum(x)
  '''
  
  '''
def lone_sum(a, b, c):

  sum = 0
  if a != b and a != c: sum += a
  if b != a and b != c: sum += b
  if c != a and c != b: sum += c
  
  return sum
  '''
  
  def lone_sum(*args):
      return sum(v for v in args if args.count(v) == 1)
	  
	  
	    
		
# Given 3 int values, a b c, return their sum. However, if one of the values is 13 then it does not count towards the sum and values to its right do not count. So for example, if b is 13, then both b and c do not count.

lucky_sum(1, 2, 3) → 6
lucky_sum(1, 2, 13) → 3
lucky_sum(1, 13, 3) → 1