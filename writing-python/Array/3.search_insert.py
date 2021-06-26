from typing import List

nums = [1,2,3,5,6]
target = 0

def brute_force(nums: List[int], target: int) -> int:
  index = 0
  while index < len(nums):
    if nums[index] >= target:
      break
    index += 1
  return index

def binary_search(nums: List[int], target: int) -> int:
  low = 0
  high = len(nums) - 1

  while low <= high:
    mid = int((low + high) / 2)

    if target == nums[mid]:
      return mid
    if target > nums[mid]:
      low = mid + 1
    if target < nums[mid]:
      high = mid - 1
  return low

# print(brute_force(nums, 4))
print(binary_search(nums,124124))