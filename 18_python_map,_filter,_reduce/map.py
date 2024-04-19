def up_name(name):
  return name.upper()

names = ["Andy", "Beni", "Adam", "Yogi"]

proper_name = []
for name in names:
  proper_name.append(up_name(name))
  
print(proper_name)

proper_name = list(map(up_name, names))
print(proper_name)

def kuadrat(n):
  return n*n

angka = [3,4,5,6]

angka_kuadrat = list(map(kuadrat, angka))
print(angka_kuadrat)