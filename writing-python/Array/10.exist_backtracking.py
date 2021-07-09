from typing import List


def exist(board: List[List[str]], word: str) -> bool:
  direction = [[-1,0], [1,0], [0, -1], [0, 1]]

  def search_direction(x: int, y: int, subword: str):
    if (x < 0 or x >= len(board)) or (y < 0 or y >= len(board[0])):
      return False
    if board[x][y] != subword[0]:
      return False
    if len(subword) == 1:
      return True

    board[x][y] = '.'

    for i,j in direction:
      if search_direction(x + i, y + j, subword[1:]):
        return True
    
    board[x][y] = subword[0]
    return False

  res = False
  for x in range(len(board)):
    for y in range(len(board[0])):
      if board[x][y] == word[0] and search_direction(x,y,word):
        res = True
        break
  return res

board = [['A', 'B', 'C', 'E'], ['S', 'F', 'S', 'D'], ['A', 'D', 'E', 'D']]
print(exist(board, "AFSE"))