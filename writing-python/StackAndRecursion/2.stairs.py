def climb_stairs(target: int, cur: int) -> int:
  if cur == target:
    return 1
  if cur > target:
    return 0
  return climb_stairs(target, cur + 1) + climb_stairs(target, cur + 2)
  
print(climb_stairs(3, 0))