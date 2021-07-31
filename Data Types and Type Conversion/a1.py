s = input()
if len(s) < 2:
  print("Empty String")
else:
  print(s[0:2]+s[len(s)-2:len(s)])
  
'''
Output
w3resource
w3ce
'''