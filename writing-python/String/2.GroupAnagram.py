from typing import List
from collections import defaultdict

def anagram(strs:List[str]) -> List[List[str]]:
  hashTable = defaultdict(list)
  for str in strs:
    hashTable["".join(sorted(str))].append(str)
  return list(hashTable.values())

def anagram2(strs:List[str]) -> List[List[str]]:
  hashTable = {}
  for str in strs:
    count = [0]*26
    for char in str:
      count[ord(char) - ord('a')] += 1;
    tup = tuple(count)
    if tup in hashTable.keys():
      hashTable[tup].append(str)
    else:
      hashTable[tup] = [str]
  print(hashTable)
  return list(hashTable.values())


strs = ['eat', 'repaid', 'paired', 'tea', 'bat']
print(anagram(strs)) 