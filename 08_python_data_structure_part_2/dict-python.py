student = {
  "name" : "Ahmad",
  "age" : 13,
  "gender" : "Male",
  "is_active" : True
}
print(student)
print(type(student))

print(student.keys())
print(student["age"])
print(student["gender"])

print("====Dictionary Manipulation=====")
# add item
student["address"] = "Jakarta"
print(student)

# change item
student["age"] = 14
print(student)

student.update({
  "color" : ["red", "black"],
  "email" : "Ahmad@mail.test"
})
print(student)

# remove item
student.pop("address")
print(student)

student.popitem()
print(student)

print("====Dictionary Constructor====")
student1 = dict(name="Jamal", age=17)
print(student1)
print(type(student1))
