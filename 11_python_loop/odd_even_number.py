num_range = int(input("Range: "))
choice = input("Even/Odd : ").lower()

if choice == "even":
  print("Even Number in the range: ")
  for i in range(num_range):
    if i % 2 == 0:
      print(i)
elif choice == "odd":
  print("Odd Number in the range: ")
  for i in range(num_range):
    if i % 2 != 0:
      print(i)
else:
  print("Invalid Choice")