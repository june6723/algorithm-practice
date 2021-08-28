def find_permutation(s):
  if len(s) == 1:
    return list(s)

  ans = []
  curr = s[0]
  s = s[1:]
  words = find_permutation(s)

  for sub in words:
    for i in range(len(sub) + 1):
      ans.append("".join([sub[:i], curr, sub[i:]]))

  return ans

def find_permutation_copy(s):
  if len(s) == 1:
    return [s]
  
  ans = []
  curr = s[0]
  s = s[1:]
  words = find_permutation_copy(s)

  for sub in words:
    for i in range(len(sub)+1):
      ans.append("".join([sub[:i], curr, sub[i:]]))
  return ans

def permutation_change_pos(s, i):
  if i + 1 == len(s):
    return [s]
  
  sub = []
  for pos in range(i, len(s)):
    if pos == i:
      sub = sub + permutation_change_pos(s, i+1)
    else:
      pos_changed = list(s)
      pos_changed[pos] = s[i]
      pos_changed[i] = s[pos]
      sub = sub + permutation_change_pos("".join(pos_changed), i+1)
  return sub

s = "abc" 
res = permutation_change_pos(s, 0)
print(*res)
