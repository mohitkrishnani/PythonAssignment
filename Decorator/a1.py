import time
def function_timer(func):
  def wrapper(*args,**kwargs):
    start = time.time()
    func()
    end = time.time()
    print(end-start," seconds")
  return wrapper

@function_timer
def f():
  a = 10
  b = 5
  print(a+b)
f()

'''Output
15
0.0009093284606933594  seconds'''