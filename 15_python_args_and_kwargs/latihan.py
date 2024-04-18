def average(*numbers):
  result = 0
  for i in numbers:
    result += i
  n = len(numbers)
  print(result/n)  

average(1,2,3,4)