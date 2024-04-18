(lambda name : print(f"Hello {name}"))("Jhon")
(lambda name : print(f"Hello {name}"))("Olive")
(lambda name : print(f"Hello {name}"))("Jack")

hello = lambda name : print("Hello", name)

hello("Nizar")
hello("Humaira")

is_even = lambda n : print("Yes") if n % 2 == 0 else print("No")

is_even(2)
is_even(13)
is_even(90)

addition = lambda x,y : x + y

add1 = addition(8,9)
print(add1)
