import string

def check_IPv4(str: str) -> str:
  arr = str.split('.')
  if len(arr) != 4:
    return 'Neither'
  for digits in arr:
    if len(digits) > 3 or len(digits) < 1:
      return 'Neither'

    if digits[0] == '0':
      if len(digits) != 1:
        return 'Neither'
    if digits.isnumeric():
      num = int(digits)
      if num > 255:
        return 'Neither'
    else: 
      return 'Neither'
  return 'IPv4'


def check_IPv6(str: str) -> str:
  arr = str.split(':')
  if len(arr) != 8:
    return 'Neither'
  for digits in arr:
    if len(digits) < 1 or len(digits) > 4 or \
      not all(c in string.hexdigits for c in digits):
      return 'Neither'
  return 'IPv6'

def IP_validation(str:str) -> str:
  if str.count('.') == 3:
    return check_IPv4(str)
  elif str.count(':') == 7:
    return check_IPv6(str);
  else:
    return 'Neither'

test = '121.125..4'
test2 = '1111:2222:3333:4444:aaaa:abbf:ADfb:bbFF'

print(IP_validation(test2))

