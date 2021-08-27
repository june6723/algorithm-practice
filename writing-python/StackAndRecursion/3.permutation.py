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

s = "abc" 
res = find_permutation(s)
print(*res)
