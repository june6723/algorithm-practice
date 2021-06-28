from typing import List

nums1 = [2,8,10]
nums2 = [5]

def brute_force(nums1: List[int], nums2: List[int]) -> None:
  n = len(nums1)
  m = len(nums2)
  k1 = 0

  for i in range(0,n):
    if nums1[k1] > nums2[0]:
      temp = nums1[k1]
      nums1[k1] = nums2[0]
      nums2[0] = temp
      k1 += 1
      nums2[:] = sorted(nums2)
    else:
      k1 += 1

brute_force(nums1,nums2)
print(nums1, nums2)
