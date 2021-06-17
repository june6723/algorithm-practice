from typing import List

nums = [2,3,8,9,11,12]
target = 13

def solution1(nums: List[int], target: int) -> List[int]: 
  for i in range(0, len(nums)):
    for j in range(i+1, len(nums)):
      if (nums[i] + nums[j]) == target:
        return [i,j]
  return [-1,-1]

def solution2(nums: List[int], target:int) -> List[int]:
  table = {}
  for i in range(0, len(nums)):
    match = target - nums[i]

    if table.get(match) is not None \
      and table[match] != i:
      return sorted([i, table[match]])
    table[nums[i]] = i
  return [-1, -1]

print(solution2(nums,target))