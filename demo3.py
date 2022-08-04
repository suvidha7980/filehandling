# writing to a file
file1 = open('myfile.txt', 'w')
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]

file1.write("Hello\n")
file1.writelines(L)
file1.close()

file1 = open('myfile.txt', 'r')
print(file1.read())
file1.close()