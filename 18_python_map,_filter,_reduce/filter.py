def even_nums(numbers):
  even_list = []
  
  for num in numbers:
    if num % 2 == 0:
      even_list.append(num)
  
  print(even_list) 

even_nums(range(1,20))

numbers = range(1,50)

def is_even(n):
  return n%2==0

even_number = list(filter(is_even,numbers))
print(even_number)    

odd_number = list(filter(lambda n : n%2 == 1, numbers))
print(odd_number)
