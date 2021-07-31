import re
def validcard(s):
  if re.match(r"^[3,4,9]\d{3}-\d{4}-\d{4}-\d{4}$",s):
    if re.search(r"(.)\1+",s) == None:
      return True
    else:
      return False
print(validcard("3245-3432-3234-2424"))
print(validcard("3245-3352-3234-2443"))

'''Output
True
False
'''