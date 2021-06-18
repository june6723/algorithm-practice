from typing import List

nums = [0,0,0,1,2,2,2]

def solution(nums:List[int]) -> int :
  answer = len(nums)
  if len(nums) > 1:
    curr = nums[0]
    answer = 1
    for i in range(1,len(nums)):
      if nums[i] != curr:
        nums[answer] = nums[i]
        curr = nums[i]
        answer += 1
  print(nums)
  return answer

print(solution(nums))