class Animal:
  name = ""
  color = ""
  
  def makeSound(self, sound):
    print(f"{self.name} is making sound {sound}")

# membuat object
cat = Animal()
cat.name = "Max"
print(cat.name)
cat.makeSound("Miowing")

dog = Animal()
dog.name = "Doggy"
dog.makeSound("Barking")


print(cat)
print(dog)
print(type(cat))

