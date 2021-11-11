# # write text
# file1 = open("texto.txt", "a")
# file1.write("Hola 1 \n")
# file1.close()
# 
# file1 = open("texto.txt", "r")
# print(file1.readlines())
# print()
# file1.close()
# 
# # Write-Overwrites
# file1 = open("texto.txt", "w")
# file1.write("Hola 2 \n")
# file1.close()
# 
# file1 = open("texto.txt", "r")
# print(file1.readlines())
# file1.close()

file1 = open("texto.txt", "w")
L = ["Cuba \n", "Espanna \n", "Italia \n"]

file1.write("Hello \n")
file1.writelines(L)
file1.close()  # to change file access modes

file1 = open("texto.txt", "r+")

print("Output of Read function is ")
print(file1.read())
print()

# seek(n) takes the file handle to the nth
# bite from the beginning.
file1.seek(0)

print("Output of Readline function is ")
print(file1.readline())
print()

file1.seek(0)

# To show difference between read and readline
print("Output of Read(9) function is ")
print(file1.read(9))
print()

file1.seek(0)

print("Output of Readline(9) function is ")
print(file1.readline(9))

file1.seek(0)

# readlines function
print("Output of Readlines function is ")
print(file1.readlines())
print()
file1.close()
