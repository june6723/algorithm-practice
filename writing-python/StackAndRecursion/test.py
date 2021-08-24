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

nums = [1, 2]
subset = [False] * len(nums)
print(group_sum(nums, subset, 3, 0))