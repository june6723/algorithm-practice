from typing import List
import copy

def subsets_recursive(nums: List[int],
  res: List[List[int]], sub:List[int], index) -> None:
  if len(sub) > len(nums):
    return
  
  res.append(sub.copy()) # sub.copy() -> sub[:]

  for i in range(index, len(nums)):
    sub.append(nums[i])
    subsets_recursive(nums, res, sub, i+1)
    sub.pop()
    


nums = [1,2,3]
res = []

subsets_recursive(nums, res, [], 0)
print(res)