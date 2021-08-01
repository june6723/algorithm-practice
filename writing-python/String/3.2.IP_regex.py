import string
import re

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

def IP_validation2(IP:str) -> str:
  IPV4 = '(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])'
  
  ipv4 = \
    re.compile(r'^({p}\.){{3}}{p}$'.format(p=IPV4))
  if ipv4.match(IP):
    return "IPv4"
  
  IPV6 = '([0-9a-f]{1,4})'

  ipv6 = \
    re.compile(r'^({p}\:){{7}}{p}$'.format(p=IPV6), re.IGNORECASE)
  
  if ipv6.match(IP):
    return "IPv6"

test = '121.125.2.4'
test2 = '256.256.256.256'
test3 = '0.0.0.0'
test4 = '1111:2222:3333:4444:aaaa:abbf:ADfb:bbFF'
test5 = '0.0.0.01'

print(IP_validation(test))
print(IP_validation(test2))
print(IP_validation(test3))
print(IP_validation(test5))


