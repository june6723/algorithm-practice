from typing import List

def missingNumber_brute(nums: List[int]) -> int:
  nums.sort()

  if nums[-1] != len(nums):
    return len(nums)
  if nums[0] != 0:
    return 0
  
  for i in range(1,len(nums)):
    if nums[i] != (nums[i-1] + 1) :
      return i

  return -1

def missingNumber_set(nums: List[int]) -> int:
  hash = set(nums)

  for i in range(len(nums)) :
    if i not in hash:
      return i
  return -1

def missingNumber_xor(nums: List[int]) -> int:
  result = len(nums)

  for i in range(len(nums)):
    result = (result^i)^nums[i]

  return result
def missingNumber_reduce(nums: List[int]) -> int:
  n = len(nums)
  sum = int(n*(n+1)/2)
  list_sum = 0
  for _,v in enumerate(nums):
    list_sum += v

  return sum - list_sum

nums = [1,0]
print(missingNumber_reduce(nums))