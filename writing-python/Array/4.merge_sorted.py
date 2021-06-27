from typing import List

def merge(nums1: List[int], nums2:List[int]) -> None:
  i = len(nums1) - len(nums2) -1
  j = len(nums2)-1
  k = i+j+1

  while i >= 0 and j >= 0:
    if nums1[i] >= nums2[j]:
      nums1[k] = nums1[i]
      i -= 1
    else:
      nums1[k] = nums2[j]
      j -= 1
    k -= 1
  while j >= 0:
    nums1[k] = nums2[j]
    j -= 1
    k -= 1

nums1 = [7,8,9,0,0,0]
nums2 = [1,2,3]
merge(nums1, nums2)
print(nums1)