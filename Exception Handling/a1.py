def raisingExcept():
  try:
    print(100/0)
  except ZeroDivisionError:
    print("Division By zero is not allowed")

  try:
    print("hello"/2)
  except TypeError:
    print("Both should be number")
  
  try:
    d = {"6":6}
    print(d["5"])
  except KeyError:
    print("Key not found")

  try:
    a = [1,2,3]
    print(a[3])
  except IndexError:
    print("Index does not exist")
  try:
    print(int("dog"))
  except ValueError:
    print("Cannot conver string to int")

raisingExcept()




'''Output
Division By zero is not allowed
Both should be number
Key not found
Index does not exist
Cannot conver string to int'''