student = {
  "name" : "Jhon",
  "address" : "Jakarta"
}

try:
  print(studt)
except NameError:
  print("Name is not defined")
except:
  print("An Error Occured!")
  
print("Exception - Else - Finally")
try:
  print(student)
except NameError:
  print("Name is not defined")
except:
  print("An Error Occured!")
else:
  print("success")
finally:
  print("Done")
  
print(50*"=")
print("Raise Exception")
loop = int(input("Enter a number: "))
try:
  if loop <= 1:
    raise Exception("Number must be > 1")
  else:
    for i in range(loop):
      print(i)
except Exception as e:
  print(e)