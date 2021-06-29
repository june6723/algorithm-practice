from typing import List

def solution(row: int) -> List[List[int]]:
  pyramid = []
  for i in range(row):
    column = []
    j = i
    while j >= 0 :
      column.append(0)
      j -= 1
    pyramid.append(column)

  pyramid[0][0] = 1
  if row == 1 :
    return pyramid
  for i in range(1,row):
    for j in range(0,i+1):
      if j == 0 or j == i:
        pyramid[i][j] = 1
      else :
        pyramid[i][j] = pyramid[i-1][j-1] + pyramid[i-1][j]
  return pyramid

print(solution(2))