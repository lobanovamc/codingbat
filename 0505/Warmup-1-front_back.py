# Given a string, return a new string where the first and last chars have been exchanged.

# front_back('code') → 'eodc'
# front_back('a') → 'a'
# front_back('ab') → 'ba'

def front_back(str):
  if len(str) > 1:
    str_1=str[0]
    str_2=str[1:-1]
    str_3=str[-1]
    return str_3+str_2+str_1
  else:
    return str