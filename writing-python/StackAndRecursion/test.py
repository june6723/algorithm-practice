nums = [1,2,3,4,5]

def sum_elements(nums):
  sum = 0
  for i in nums:
    sum = sum + i
  return sum

print(sum_elements(nums))

def sum_recursion(nums):
  if len(nums) == 0:
    return 0
  if len(nums) == 1:
    return nums[0]

  return nums[0] + sum_recursion(nums[1:])

print(sum_recursion(nums))