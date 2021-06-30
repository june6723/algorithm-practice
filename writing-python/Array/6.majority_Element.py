from typing import List
import math

def solution1(nums: List[int]) -> int:
  length = len(nums)
  threshold = math.ceil(length/2)

  if length == 1:
    return nums[0]
  else:
    for i in range(0, length):
      target = nums[i]
      times = 1
      for j in range(i+1, length):
        if (target == nums[j]):
          times += 1
          if times >= threshold:
            return target

def answer_in_book(nums: List[int]) -> int:
  majority_count = int(len(nums)/2)

  for i, item_i in enumerate(nums):
    count = 0
    for j, item_j in enumerate(nums[i:], start=i):
      if item_i == item_j:
        count += 1
      if count > majority_count:
        return item_i
  return -1

def solution2(nums: List[int]) -> int:
  length = len(nums)
  threshold = math.ceil(length/2)
  hashmap = {}

  if length == 1:
    return nums[0]
  else:
    for i in range(0, length):
      target = nums[i]
      if target in hashmap.keys():
        hashmap[target] += 1
        if hashmap[target] >= threshold:
          return target
      else :
        hashmap[target] = 1

def answer_in_book(nums: List[int]) -> int:
  majority_count = int(len(nums)/2)

  hashmap = {}

  for num in nums:
    if hashmap.get(num) != None:
      hashmap[num] = hashmap[num] + 1
    else:
      hashmap[num] = 1

    if hashmap[num] > majority_count:
      return num

  return -1

def solution3(nums: List[int]) -> int:
  return sorted(nums)[int(len(nums)/2)]

test_set = [1]
test_set2 = [2,3,6,4,4,4,4,4]
print(solution3(test_set2))
