# multiple inheritance
class a :
  def fun1(self):
    print("day1")
class b:
  def fun2(self):
    print("day2")
class c(a,b):
  pass
obj=a()
obj2= b()
obj.fun1()
obj2.fun2()
