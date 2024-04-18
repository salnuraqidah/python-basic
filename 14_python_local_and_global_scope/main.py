x = 10 # global variable

def test_global_scope():
  print(x)

print(x) 
test_global_scope()

score = 0
def test_local_scope():
  global x, score
  x += 1
  n = 99
  score+=1
  print(n)
  print(x)

print("===")
test_local_scope()
test_local_scope()
test_local_scope()
print(x)
print(score)

