with open("19_python_file_handling/My Bio.txt", "w") as file:
  file.write('Nama Saya Salamah. ')
  file.write('Domisili saya di Bekasi.')
  
read_file = open("19_python_file_handling/My Bio.txt", "r")
print(read_file.read())

  