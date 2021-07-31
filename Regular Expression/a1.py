import re
def dateCheck(date):
  if re.match(r"^\w{3,9}\s\d{1,2},\s\d+$",date):
    return True
  else:
    return False

print(dateCheck("July 03, 2007"))

'''output
True'''