# create
try:
  file = open("19_python_file_handling/newFile.txt", "x")
except FileExistsError:
  print("File sudah ada")
  

# read
file_read = open("19_python_file_handling/newFile.txt", "r")

print(file_read.read())

# write
file = open("19_python_file_handling/newFile.txt", "w")
text = "Python is a programming language"
file.write(text)

file.close()

file2 = open("19_python_file_handling/note.txt", "w")
text = "Python is a programming language!!"
file2.write(text)

file2.close()

# append

a = open("19_python_file_handling/newFile.txt", "a")
a.write("\nAlhazen Academy")

a.close()