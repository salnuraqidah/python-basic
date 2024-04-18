number = 1

while number < 10:
  print("I Like Python")
  number += 1

names = ["Andi","Beni","Chika"]

for name in names:
  print(name)
  
for i in range(10):
  print("I like python")

print("Loop-Break")
num = 1

while num<10:
  print(num)
  if num == 3:
    break
  num+=1
  
print("====Loop-Continue=====")
num = 1

while num<10:
  num+=1
  if num == 3:
    continue
  print(num)
  
for i in range(1,10):
  if i == 3:
    continue
  print(i)

print("===For Else===")
name = "Jaka"

for letter in name:
  print(letter)
else:
  print("done")
  
for i in range(10):
  pass

print("===Nested Loop===")
fruits = ["Apple", "Banana","Cherry"]
colors = ["Green", "Yellow", "Red"]

for color in colors:
  for fruit in fruits:
    print(color, fruit)
    
  