print("Arbitrary Argument")

def addition(*numbers):
  result = 0
  for i in numbers:
    result += i
  print(result)  

addition(1,2,3)

def sayHello(fname, lname):
  print(f"Hello {fname} {lname}")
  
sayHello(lname="Academy", fname="Alhazen")

print(50*"=")
print("Arbitrary Keyword Argument")

def student(**data):
  result = data.values()
  print(" ".join(result))
  
student(
  name = "Alhazen",
  age = "13",
  address = "Jakarta"
)

print(50*"=")
print("Default Value")

def greeting(name, message = "Hello"):
  print(message, name)

greeting("Nur")
greeting("Nur", "Hai")
