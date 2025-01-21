# a = lambda x,y : x * y

# print(a(2,3))


# def myfunc(n):
#   return lambda a : a - n

# mydoubler = myfunc(2)

# print(mydoubler(11))


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def is_senior_citizen(self):
    if self.age > 60:
      print("Senior Citizen")
    else:
      print("Not a Senior Citizen")


p1 = Person("John", 36)
print(p1.name)
print(p1.age)
p1.is_senior_citizen()

