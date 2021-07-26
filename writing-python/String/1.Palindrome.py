def isPalindrome(s: str) -> bool:
  i = 0
  j = len(s) -1

  s = s.lower()

  while i < j:
    while i < j:
      if s[i].isalnum():
        break
      i += 1
    
    while i<j:
      if s[j].isalnum():
        break
      j -= 1

    if s[i] != s[j]:
      return False

    i += 1
    j -= 1

  return True

def isPalindrome2(s: str) -> bool:
  filtered = "".join(list(filter(str.isalnum, s))).lower()
  return filtered == filtered[::-1]

# print(isPalindrome('a.bb,.c/c/,b.,.ba'))
print(isPalindrome2('a.bb,.c/c/,b.,.ba'))
print(isPalindrome2('.,//`.-/.,='))