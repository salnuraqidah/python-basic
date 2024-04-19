from functools import reduce

def addition(number1, number2):
  return number1+number2

numbers = range(1,11)

hasil = reduce(addition, numbers)
print(hasil)