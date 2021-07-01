from typing import List


def brute_force(nums: List[int], k: int) -> None:
  for _ in range(k):
    prev = nums[len(nums) - 1]
    for i in range(len(nums)):
      temp = nums[i]
      nums[i] = prev
      prev = temp

def save_on_empty_arr(nums: List[int], k: int) -> List[int]:
  temp = [0] * len(nums)

  for i in range(len(nums)):
    temp[(i+k)%len(nums)] = nums[i]
  return temp

def rotate_in_arr(nums: List[int], k: int) -> None:
  count = 0
  
  for start in range(len(nums)):
    if count >= len(nums):
      break
    
    curr_index = start
    prev_value = nums[start]
    while True:
      next_index = (curr_index+k) % len(nums)
      temp = nums[next_index]
      nums[next_index] = prev_value
      prev_value = temp

      count += 1
      curr_index = next_index

      if curr_index == start:
        break;

def reverse_3(nums: List[int], k: int) -> None:
  k = k % len(nums)
  nums[:] = nums[::-1]
  nums[0:k] = nums[0:k][::-1]
  nums[k:len(nums)] = nums[k:len(nums)][::-1]


nums = [1,2,3,4,5,6]
k = 2
reverse_3(nums,k)
print(nums)