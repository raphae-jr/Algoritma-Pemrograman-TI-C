class Person:
  def __init__(self, name, salary):
    self.name = name
    self._salary = salary  # Protected property

p1 = Person("Linus", 50000)
print(p1.name)
print(p1._salary)  # Can access, but shouldn't


class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age  # Private property

p1 = Person("Emil", 25)
print(p1.name)
print(p1.__age)  # This will cause an error
