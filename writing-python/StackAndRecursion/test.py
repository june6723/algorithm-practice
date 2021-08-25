from typing import List


def group_sum(nums: List[int], subset: List[bool], target: int, i: int) -> bool:
  if i == len(nums):
    subset_sum = 0
    for i, v in enumerate(nums):
      if subset[i]:
        subset_sum += v
    return (subset_sum == target)
  
  subset[i] = False
  not_select = group_sum(nums, subset, target, i + 1)
  subset[i] = True
  select = group_sum(nums, subset, target, i + 1)

  return (not_select | select)

def group_sum_copy(nums: List[int], subset: List[bool], target: int, i: int) -> bool:
  if len(nums) is i:
    sum = 0
    for i, v in enumerate(nums):
      if subset[i]:
        sum += nums[i]
    return target == sum
  
  subset[i] = False
  without_value = group_sum_copy(nums, subset, target, i + 1)
  subset[i] = True
  with_value = group_sum_copy(nums, subset, target, i + 1)

  return (with_value | without_value) 

nums = [1, 2, 3]
subset = [False] * len(nums)
print(group_sum_copy(nums, subset, 7, 0))