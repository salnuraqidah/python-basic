print('====SET====')
numbers = {0, 1, 2, 3, 4, 5}
fruits = {"Cherry", "Durian", "Apple", "Melon"}
data = {"Alhazen", True, 5}

print(numbers)
print(type(numbers))
print(len(numbers))

print(fruits)
print(data)

# access value
# print(data[2]) # error : cannot be access with index

# access value with loop
for i in fruits:
  print(i)
  
print("======SET Manipulation=====")
# add item
fruits.add("Orange")
print(fruits)

# remove item
fruits.discard("Durian")
fruits.discard("Avocado")
print(fruits)

fruits.remove("Melon")
# fruits.remove("Avocado") # error
print(fruits)

fruits.pop()
print(fruits)

print("=====Add Item in Existing Set====")
names = {"Ahmad", "Humaira", "Syafiq"}
friend_name = {"Fatih", "Bobby", "Jack"}

friend_list = {"Hamzah", "Galang", "Rofi"}
names.update(friend_name)
names.update(friend_list)
print(names)

print("===SET Constructor====")
cars = set(("Toyota","Honda","Suzuki"))
print(cars)
print(type(cars))