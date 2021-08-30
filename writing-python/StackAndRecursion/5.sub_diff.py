from typing import List

def sub_diff(nums: List[int]) -> int:
  sumAll = 0
  for num in nums:
    sumAll += num
  def diff_recur(nums: List[int], diff: int, i:int):
    if i == len(nums) - 1:
      return abs(diff)
    curr = nums[i]
    not_select = diff_recur(nums, diff, i+1)
    select = diff_recur(nums, diff - 2*curr, i+1)

    return min(not_select, select)

  return diff_recur(nums, sumAll, 0)
    
nums = [3,2,1,4]
print(sub_diff(nums))