import random

# defining a class
class Dog:
  
  # __init__() method and instance attributes
  def __init__(self, name, age):
    self.name = name
    self.age = age
    self.tricks = []
    self.isSitting = False

  # custom instance methods
  def learn_trick(self, new_trick):
    self.tricks.append(new_trick)

  def do_trick(self):
    if len(self.tricks) == 0:
      return self.name + " doesn't know any tricks!"
    else:
      num = random.randint(0, len(self.tricks) - 1)
      return self.tricks[num]

  def sit_down(self):
    self.isSitting = True

  def stand_up(self):
    self.isSitting = False

  def get_state(self):
    if self.isSitting:
      return self.name + " is sitting"
    else:
      return self.name + " is standing"

  # __str__() method
  def __str__(self):
    ret = "Name: " + self.name + " | Age: " + str(self.age) + " | Tricks: " + str(self.tricks) + " | State: "
    if self.isSitting:
      return ret + "Sitting"
    else:
      return ret + "Standing"
  

# test __init__() and instance attributes
toto = Dog("Fido", 4)
print(toto.name)
print(toto.age)
print(toto.tricks)
print(toto.isSitting)
print()

toto.name = "Toto"
toto.age = 7
toto.tricks = ["play catch"]
toto.isSitting = False

print(toto.name)
print(toto.age)
print(toto.tricks)
print(toto.isSitting)
print()

# test custom instance methods
toto.learn_trick("Roll Over")
print(toto.do_trick())
toto.stand_up()
print(toto.get_state())
toto.sit_down()
print(toto.get_state())
print()

# test __str__() method
print(toto)
