today = "sunny"

if today == "sunny":
  print("I don't have use umbrella")
  
battery_level = "full"

if battery_level == "low":
  print("Charge your battery..")
else:
  print("Full Charge..")

print("Input your grade A/B/C")
grade = input("Grade: ").upper()

if grade == "A":
  print("Congratulation..")
elif grade == "B":
  print("Good Job..")
elif grade == "C":
  print("Good luck next time..")
else:
  print("Wrong input")


score = 76

if score > 85 and score <= 100:
  print("A")
elif score > 70 and score < 85:
  print("B")
else:
  print("C")
  
money = 5000

if money == 5000 or money > 8000:
  print("Buy programming book!")
else:
  print("Save more money!")
  
print("====Nested If====")
age = 18
driver_lisence = False

if age > 17:
  print("user is teeneger")
  if driver_lisence == True:
    print("And driving is allowed")
  else:
    print("And driving is not allowed")
else:
  print("user is not yet a teenager")
  
# https://gist.github.com/versimalik/52d8370f921ac912d474d0af2d66ca6d