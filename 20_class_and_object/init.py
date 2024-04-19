class Animal:
  
  def __init__(self, name, color):
    self.name = name
    self.color = color
      
  def makeSound(self, sound):
    print(f"{self.name} with color {self.color} is making sound {sound}")
    
  def eat(self, food):
    print(f"{self.name} is eating {food}")
    

cat = Animal("Kitty", "Yellow")
cat.makeSound("Miowing")
cat.eat("fish")

dog = Animal("Bravo", "Black")
dog.makeSound("Barking")
dog.eat("snack")

bird = Animal("Tweety", "Brown")
bird.makeSound("Chirping")
bird.eat("corn")