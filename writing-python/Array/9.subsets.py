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
    
def subsets_binary(nums: List[int]) -> List[List[int]]:
  res = []
  nums_len = len(nums)
  nth_bit = 1 << nums_len

  for i in range(2 ** nums_len):
    bitmask = bin(i | nth_bit)[3:]

    res.append(
      [nums[j] for j in range(nums_len) if bitmask[j] == '1']
    )
  return res


nums = [1,2,3]
res = []

subsets_recursive(nums, res, [], 0)
print(res)
print(subsets_binary(nums))