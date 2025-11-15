# encapsulation
class family:
  def __init__(self):
    self.public = 25
    self.__private = 37
  def function(self):
    print(self.__private)
object1=family()
print(object1.public)
object1.function()
