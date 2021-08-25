def check_valid_brackets(brackets: str) -> bool:
  stack = []
  opens = ['(', '{', '[']
  closes = [')', '}', ']']

  if len(brackets) == 0:
    return True
  for _, char in enumerate(brackets):
    if char in opens:
      stack.append(char)
    if char == ')':
      if stack.pop() != '(':
        return False
    if char == '}':
      if stack.pop() != '{':
        return False
    if char == ']':
      if stack.pop() != '[':
        return False
  return True

test1 = '({([])})'
test2 = '(){(}[])'
print(check_valid_brackets(test1))
print(check_valid_brackets(test2))