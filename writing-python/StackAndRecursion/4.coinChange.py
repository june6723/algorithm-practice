from typing import List
import sys

def coinChange(coinType: List[int], change: int): 
  ans = [0] * len(coinType)
  def calculate_min_coins(i:int, change: int, ans: List[int]):  
    if change <= 0:
      return
    currCoin = coinType[i]
    left = change - currCoin
    if left >= 0:
      ans[i] += 1
      calculate_min_coins(i, left, ans)
    else:
      calculate_min_coins(i - 1, change, ans)
    
  calculate_min_coins(len(coinType)-1, change, ans)
  return ans

def coinChange2(coins: List[int], value: int) -> int:
  def change(v: int):
    if v == 0:
      return 0
    min_coin_cnt = sys.maxsize
    for c in coins: 
      if (v - c) >= 0:
        change_cnt = change(v - c)
        if change_cnt < min_coin_cnt:
          min_coin_cnt = change_cnt
    return min_coin_cnt + 1
  ans = change(value)

  return ans if ans != sys.maxsize + 1 else -1

# print(coinChange([1,2,5], 11));
print(coinChange2([1,2], 11));