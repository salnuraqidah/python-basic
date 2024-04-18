def countDown(number):
  print(number)
  if number == 0:
    return
  else:
    countDown(number-1)
    
countDown(10)

def factorial(number):
  if number <= 1:
    return 1
  else:
    result = number * factorial(number-1)
    return result

hasil = factorial(5)
print(hasil)